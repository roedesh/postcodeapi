import pytest

from postcodeapi.client import PostcodeAPIClient


@pytest.fixture
def api_client():
    return PostcodeAPIClient(api_key="SOME_KEY")


@pytest.fixture
def api_client_without_key():
    return PostcodeAPIClient(api_key="")