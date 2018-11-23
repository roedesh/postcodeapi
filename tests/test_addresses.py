import pytest
import requests

from postcodeapi.exceptions import HouseNumberRequiresPostalCode, InvalidPostalCode
from tests.mock_addresses import (
    mock_address,
    mock_all_addresses,
    mock_all_addresses_from_postal_code,
    mock_postal_code_missing,
)


def test_get_address(monkeypatch, api_client):
    monkeypatch.setattr(requests, "get", mock_address)
    data = api_client.get_address(address_id="0855200000046355")
    assert data["postcode"] == "5038EA"


def test_get_address_invalid_postal_code(monkeypatch, api_client):
    monkeypatch.setattr(requests, "get", mock_address)
    with pytest.raises(InvalidPostalCode):
        api_client.get_all_addresses(postal_code="NOT A POSTAL CODE")


def test_get_all_addresses(monkeypatch, api_client):
    monkeypatch.setattr(requests, "get", mock_all_addresses)
    addresses = api_client.get_all_addresses()
    assert addresses["next"]
    assert addresses["entries"][0]["postcode"] == "3815MB"


def test_get_all_addresses_from_postal_code(monkeypatch, api_client):
    monkeypatch.setattr(requests, "get", mock_all_addresses_from_postal_code)
    addresses = api_client.get_all_addresses(postal_code="5038EA")
    assert addresses["entries"][0]["postcode"] == "5038EA"


def test_get_all_addresses_postal_code_missing(monkeypatch, api_client):
    monkeypatch.setattr(requests, "get", mock_postal_code_missing)
    with pytest.raises(HouseNumberRequiresPostalCode):
        api_client.get_all_addresses(number=30)
