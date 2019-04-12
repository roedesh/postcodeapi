import pytest
import requests_mock
from postcodeapi.exceptions import InvalidPostalCode, ResourceNotFound

from tests.unit_tests.helpers import read_file


def test_get_all_postal_codes(api_client):
    with requests_mock.mock() as m:
        m.get(
            "https://api.postcodeapi.nu/v2/postcodes",
            text=read_file("postal_code_list.json"),
        )
        data = api_client.get_all_postal_codes()["results"]
        assert data[0]["postcode"] == "7315AA"


def test_get_all_postal_codes(api_client):
    with requests_mock.mock() as m:
        m.get(
            "https://api.postcodeapi.nu/v2/postcodes?from[postcode]=7315AA&from[postcodeArea]=7315",
            text=read_file("postal_code_list_from_postal_code.json"),
        )
        data = api_client.get_all_postal_codes(from_postal_code="7315AA")["results"]
        assert data[0]["postcode"] == "7315BB"


def test_get_all_postal_codes_invalid_from_postal_code(api_client):
    with pytest.raises(InvalidPostalCode):
        api_client.get_all_postal_codes(from_postal_code="NOT A POSTAL CODE")


def test_get_all_postal_codes_area(api_client):
    with requests_mock.mock() as m:
        m.get(
            "https://api.postcodeapi.nu/v2/postcodes?postcodeArea=7313",
            text=read_file("postal_code_list_area.json"),
        )
        data = api_client.get_all_postal_codes(area="7313")["results"]
        assert data[0]["postcode"] == "7513AA"


def test_get_postal_code(api_client):
    with requests_mock.mock() as m:
        m.get(
            "https://api.postcodeapi.nu/v2/postcodes/7315AD",
            text=read_file("single_postal_code.json"),
        )
        data = api_client.get_postal_code(postal_code="7315AD")
        assert data["postcode"] == "7315AD"


def test_get_postal_code_invalid_postal_code(api_client):
    with pytest.raises(InvalidPostalCode):
        api_client.get_postal_code(postal_code="NOT A POSTAL CODE")


def test_get_postal_code_not_found(api_client):
    with pytest.raises(ResourceNotFound), requests_mock.mock() as m:
        m.get(
            "https://api.postcodeapi.nu/v2/postcodes/1234AB",
            text=read_file("error_resource_not_found.json"),
            status_code=404,
        )
        api_client.get_postal_code(postal_code="1234AB")