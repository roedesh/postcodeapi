import json
from urllib.parse import parse_qs, urlencode, urlparse

import requests

from postcodeapi import exceptions
from postcodeapi.utils import is_valid_postal_code

POSTCODE_API_V2_URL = "https://api.postcodeapi.nu/v2/"
POSTCODE_API_ALL_ADDRESSES = "addresses"
POSTCODE_API_ADDRESS = "addresses/{}"
POSTCODE_API_ALL_POSTAL_CODES = "postcodes"
POSTCODE_API_POSTAL_CODE = "postcodes/{}"


def generate_list_result(data, identifier="addresses"):
    """Generate a dictionary with the results and the next id or
    postal code if it's available.


    Arguments:
        data {dict} -- Data dictionary

    Keyword Arguments:
        identifier {str} -- Dictionary key which holds the results (default: {"addresses"})

    Returns:
        dict -- Dictionary with the results and the next id or
                postal code
    """

    results = data.get("_embedded", {}).get(identifier, {})
    next_url = data.get("_links", {}).get("next", {}).get("href", "")

    # Extract the id or postal code from the "next" url querystring
    if next_url:
        parsed_qs = parse_qs(urlparse(next_url).query)
        if identifier == "addresses":
            next_val = parsed_qs.get("from[id]", None)
        else:
            next_val = parsed_qs.get("from[postcode]", None)
    else:
        next_val = None

    return {"results": results, "next": next_val}


class PostcodeAPIClient:
    """
    A wrapper around the Postcode API V2.
    It allows for filtering trough addresses and postal codes.

    All getter methods return JSON data as a Python dictionary.

    Full documentation can be found on https://www.postcodeapi.nu/docs/
    """

    def __init__(self, api_key):
        """
        Initializes a new API client for the Postcode API v2. Requires an API key.
        Upon initialization the required headers will be pre-set for later use.

        :param api_key: Postcode API V2 key
        """
        self._headers = {
            "x-api-key": api_key,
            "accept": "application/hal+json",
        }

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
            raise exceptions.NoAccessException(
                "The current account is not allowed to do this"
            )
        if response.status_code == 404:
            raise exceptions.ResourceNotFoundException("Object not found")
        if response.status_code == 429:
            raise exceptions.LimitExceededException(
                "Limit exceeded or too many requests"
            )
        return json.loads(data)

    def get_all_addresses(self, postal_code=None, number=0, from_id=None):
        """
        Return a list of addresses. Can be filtered by providing a postal code and house number.
        Filtering on a house number requires a postal code

        :param postal_code: (Optional) Postal code to filter on
        :param number: (Optional) House number to filter on
        :param from_id: (Optional) The address ID to start from
        :return: List of address dictionaries
        """
        querystring = {}

        if number:
            if not postal_code:
                raise exceptions.HouseNumberRequiresPostalCodeException(
                    "Filtering on a house number requires a postal code"
                )
            querystring.update({"number": number})

        if postal_code:
            if not is_valid_postal_code(postal_code):
                raise exceptions.InvalidPostalCodeException(
                    "postal_code should be a valid Dutch postal code"
                )
            querystring.update({"postcode": postal_code})

        if from_id:
            querystring.update({"from[id]": from_id})

        data = self._do_request(POSTCODE_API_ALL_ADDRESSES, querystring)
        return generate_list_result(data, "addresses")

    def get_address(self, address_id):
        """
        Return a single address based on the given ID.

        :param address_id: ID of the address
        :return: Single address based on ID
        """
        return self._do_request(POSTCODE_API_ADDRESS.format(address_id))

    def get_all_postal_codes(self, area=None, from_postal_code=None):
        """
        Return a list of postal codes. Can be filtered based on a given postal area.

        :param area: Postal area to filter on
        :param from_postal_code: (Optional) The postal code to start from
        :return: List of postal code dictionaries
        """
        if from_postal_code and not is_valid_postal_code(from_postal_code):
            raise exceptions.InvalidPostalCodeException(
                "from_postal_code should be a valid Dutch postal code"
            )

        querystring = {}
        if area:
            querystring.update({"postcodeArea": area})

        if from_postal_code:
            querystring.update(
                {
                    "from[postcode]": from_postal_code,
                    # We need to provide both from[postcode] and from[postcodeArea] in order for pagination to work
                    # So we use the four numbers from the postal code as the area code
                    "from[postcodeArea]": from_postal_code[:4],
                }
            )
        data = self._do_request(POSTCODE_API_ALL_POSTAL_CODES, querystring)
        return generate_list_result(data, "postcodes")

    def get_postal_code(self, postal_code):
        """
        Return a single postal code based on the given postal code.

        :param postal_code: Postal code to lookup
        :return: Single postal code
        """
        if not is_valid_postal_code(postal_code):
            raise exceptions.InvalidPostalCodeException(
                "postal_code should be a valid Dutch postal code"
            )
        return self._do_request(POSTCODE_API_POSTAL_CODE.format(postal_code))
