import pytest
import requests

from postcodeapi.exceptions import NoAccess, ResourceNotFound
from tests.mock_generic import mock_forbidden, mock_resource_not_found


def test_no_access(monkeypatch, api_client):
    monkeypatch.setattr(requests, "get", mock_forbidden)
    with pytest.raises(NoAccess):
        api_client.get_all_addresses()

    with pytest.raises(NoAccess):
        api_client.get_address(address_id="ID")

    with pytest.raises(NoAccess):
        api_client.get_all_postal_codes()

    with pytest.raises(NoAccess):
        api_client.get_postal_code(postal_code="7315AD")


def test_resource_not_found(monkeypatch, api_client):
    monkeypatch.setattr(requests, "get", mock_resource_not_found)

    with pytest.raises(ResourceNotFound):
        api_client.get_address(address_id="ID")

    with pytest.raises(ResourceNotFound):
        api_client.get_postal_code(postal_code="7315AD")
