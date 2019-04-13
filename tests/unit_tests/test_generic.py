import pytest
import requests_mock

from postcodeapi.exceptions import (LimitExceededException, NoAccessException,
                                    ResourceNotFoundException)


def test_no_access(api_client):
    with requests_mock.mock() as m:
        m.register_uri(requests_mock.ANY, requests_mock.ANY, status_code=403)

        with pytest.raises(NoAccessException):
            api_client.get_all_addresses()

        with pytest.raises(NoAccessException):
            api_client.get_address(address_id="ID")

        with pytest.raises(NoAccessException):
            api_client.get_all_postal_codes()

        with pytest.raises(NoAccessException):
            api_client.get_postal_code(postal_code="7315AD")


def test_resource_not_found(api_client):
    with requests_mock.mock() as m:
        m.register_uri(requests_mock.ANY, requests_mock.ANY, status_code=404)

        with pytest.raises(ResourceNotFoundException):
            api_client.get_address(address_id="ID")

        with pytest.raises(ResourceNotFoundException):
            api_client.get_postal_code(postal_code="7315AD")


def test_limit_exceeded(api_client):
    with requests_mock.mock() as m:
        m.register_uri(requests_mock.ANY, requests_mock.ANY, status_code=429)

        with pytest.raises(LimitExceededException):
            api_client.get_address(address_id="ID")

        with pytest.raises(LimitExceededException):
            api_client.get_all_addresses()

        with pytest.raises(LimitExceededException):
            api_client.get_postal_code(postal_code="7315AD")

        with pytest.raises(LimitExceededException):
            api_client.get_all_postal_codes()
