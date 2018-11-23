import json
import urllib
from urllib.parse import urlencode

import requests

from postcodeapi import exceptions
from postcodeapi.utils import is_valid_dutch_postal_code

POSTCODE_API_V2_URL = "https://api.postcodeapi.nu/v2/"
POSTCODE_API_ALL_ADDRESSES = "addresses"
POSTCODE_API_SINGLE_ADDRESS = "addresses/{}"
POSTCODE_API_ALL_POSTAL_CODES = "postcodes"
POSTCODE_API_SINGLE_POSTAL_CODE = "postcodes/{}"


def _extract_next_from_postal_code(next_url):
    decoded_url = urllib.parse.unquote(next_url)
    return decoded_url.split("&from[postcodeArea]")[0][-6:]


def _extract_next_from_address(next_url):
    decoded_url = urllib.parse.unquote(next_url)
    return decoded_url.split("?from[id]=")[1]


class PostcodeAPIClient:
    """
    A wrapper around the Postcode API V2.
    It allows to filter trough addresses and postal codes.

    All getter methods return JSON data as a Python object.

    Full documentation can be found on https://www.postcodeapi.nu/docs/
    """

    def __init__(self, api_key, compact=False):
        """
        Initializes a new API client for the Postcode API v2. Requires an API key.
        Upon initialization the required headers will be pre-set for later use.

        :param api_key: Postcode API V2 key
        """
        self._headers = {"x-api-key": api_key, "accept": "application/hal+json"}
        self.compact = compact

    def _do_request(self, endpoint, querystring=None):
        """
        Starts a GET request and returns the JSON data converted to a Python dictionary.

        :param endpoint: Endpoint to call
        :param querystring: (Optional) The querystring to pass
        :return: JSON data converted to Python dictionary
        """
        response = requests.get(
            POSTCODE_API_V2_URL + endpoint,
            headers=self._headers,
            params=urlencode(querystring or {}),
        )
        data = response.text
        if response.status_code == 403:
            raise exceptions.NoAccess
        if response.status_code == 404:
            raise exceptions.ResourceNotFound
        return json.loads(data)

    def get_all_addresses(self, postal_code=None, number=0, from_id=""):
        """
        Return a list of addresses. Can be filtered by providing a postal code and/or house number.
        Filtering on a house number requires a postal code

        :param postal_code: Postal code to filter on
        :param number: (Optional) House number to filter on
        :param from_id: (Optional) The address ID to start from
        :return: List of address dictionaries
        """
        if number and not postal_code:
            raise exceptions.HouseNumberRequiresPostalCode
        if postal_code and not is_valid_dutch_postal_code(postal_code):
            raise exceptions.InvalidPostalCode
        querystring = {"postcode": postal_code, "number": number, "from[id]": from_id}
        data = self._do_request(POSTCODE_API_ALL_ADDRESSES, querystring)
        entries = data["_embedded"]["addresses"]
        next_from_address = (
            _extract_next_from_address(data["_links"]["next"]["href"])
            if "next" in data["_links"]
            else ""
        )

        return {"entries": entries, "next": next_from_address}

    def get_address(self, address_id):
        """
        Return a single address based on the given ID.

        :param address_id: ID of the address
        :return: Single address based on ID
        """
        return self._do_request(POSTCODE_API_SINGLE_ADDRESS.format(address_id))

    def get_all_postal_codes(self, area=None, from_postal_code=""):
        """
        Return a list of postal codes. Can be filtered based on a given postal area.

        :param area: Postal area to filter on
        :param from_postal_code: (Optional) The postal code to start from
        :return: List of postal code dictionaries
        """
        if from_postal_code and not is_valid_dutch_postal_code(from_postal_code):
            raise exceptions.InvalidPostalCode
        querystring = {
            "postcodeArea": area,
            "from[postcode]": from_postal_code,
            # We need to provide both from[postcode] and from[postcodeArea] in order for pagination to work
            # So we use the four numbers from the postal code as the area code
            "from[postcodeArea]": from_postal_code[:4],
        }
        data = self._do_request(POSTCODE_API_ALL_POSTAL_CODES, querystring)
        entries = data["_embedded"]["postcodes"]
        next_from_postal_code = (
            _extract_next_from_postal_code(data["_links"]["next"]["href"])
            if "next" in data["_links"]
            else ""
        )
        return {"entries": entries, "next": next_from_postal_code}

    def get_postal_code(self, postal_code):
        """
        Return a single postal code based on the given postal code.

        :param postal_code: Postal code to lookup
        :return: Single postal code
        """
        if not is_valid_dutch_postal_code(postal_code):
            raise exceptions.InvalidPostalCode
        return self._do_request(POSTCODE_API_SINGLE_POSTAL_CODE.format(postal_code))
