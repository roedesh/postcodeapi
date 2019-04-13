import pytest

from postcodeapi.client import PostcodeAPIClient


@pytest.fixture
def api_client():
    return PostcodeAPIClient(api_key="YOUR_KEY")
