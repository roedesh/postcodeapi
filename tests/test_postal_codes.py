import pytest
import requests

from postcodeapi.exceptions import InvalidPostalCode, ResourceNotFound
from tests.mock_generic import mock_resource_not_found
from tests.mock_postal_codes import (
    mock_all_postal_codes,
    mock_all_postal_codes_area,
    mock_postal_code,
)


def test_get_all_postal_codes(monkeypatch, api_client):
    monkeypatch.setattr(requests, "get", mock_all_postal_codes)
    data = api_client.get_all_postal_codes()
    assert data["_embedded"]["postcodes"][0]["postcode"] == "7315AA"


def test_get_all_postal_codes_invalid_from_postal_code(monkeypatch, api_client):
    monkeypatch.setattr(requests, "get", mock_all_postal_codes)
    with pytest.raises(InvalidPostalCode):
        api_client.get_all_postal_codes(from_postal_code="NOT A POSTAL CODE")


def test_get_all_postal_codes_area(monkeypatch, api_client):
    monkeypatch.setattr(requests, "get", mock_all_postal_codes_area)
    data = api_client.get_all_postal_codes(area="7313")
    assert data["_embedded"]["postcodes"][0]["postcode"] == "7513AA"


def test_get_postal_code(monkeypatch, api_client):
    monkeypatch.setattr(requests, "get", mock_postal_code)
    data = api_client.get_postal_code(postal_code="7315AD")
    assert data["postcode"] == "7315AD"


def test_get_postal_code_invalid_postal_code(monkeypatch, api_client):
    monkeypatch.setattr(requests, "get", mock_postal_code)
    with pytest.raises(InvalidPostalCode):
        api_client.get_postal_code(postal_code="NOT A POSTAL CODE")


def test_get_postal_code_not_found(monkeypatch, api_client):
    monkeypatch.setattr(requests, "get", mock_resource_not_found)
    with pytest.raises(ResourceNotFound):
        api_client.get_postal_code(postal_code="1234AB")
