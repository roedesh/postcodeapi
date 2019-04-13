import pytest
import requests_mock

from postcodeapi.exceptions import (HouseNumberRequiresPostalCodeException,
                                    InvalidPostalCodeException)
from tests.unit_tests.helpers import get_api_url, read_file


def test_get_address(api_client):
    with requests_mock.mock() as m:
        m.get(
            get_api_url("addresses/0855200000046355"),
            text=read_file("single_address.json"),
        )
        data = api_client.get_address(address_id="0855200000046355")
        assert data["postcode"] == "5038EA"


def test_get_address_invalid_postal_code(api_client):
    with pytest.raises(InvalidPostalCodeException):
        api_client.get_all_addresses(postal_code="AB1234")


def test_get_all_addresses(api_client):
    with requests_mock.mock() as m:
        m.get(get_api_url("addresses"), text=read_file("address_list.json"))
        data = api_client.get_all_addresses(postal_code="5038EA")["results"]
        assert data[0]["postcode"] == "5038EA"


def test_get_all_addresses_with_postal_code_and_number(api_client):
    with requests_mock.mock() as m:
        m.get(
            get_api_url("addresses?postcode=6545CA&number=5"),
            text=read_file("address_list_postal_code_and_number.json"),
        )
        data = api_client.get_all_addresses(postal_code="6545CA", number=5)["results"]
        assert data[0]["postcode"] == "6545CA"
        assert data[0]["number"] == 5


def test_get_all_addresses_from_id(api_client):
    with requests_mock.mock() as m:
        m.get(
            get_api_url("addresses?from[id]=0503200000060096"),
            text=read_file("address_list_from_id.json"),
        )
        data = api_client.get_all_addresses(from_id="0503200000060096")["results"]
        assert data[0]["id"] == "0553200000001332"


def test_get_all_addresses_postal_code_missing(api_client):
    with pytest.raises(HouseNumberRequiresPostalCodeException):
        api_client.get_all_addresses(number=30)
