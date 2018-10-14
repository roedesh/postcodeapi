import collections

MockResponse = collections.namedtuple("MockResponse", ["status_code", "text"])


def mock_resource_not_found(*args, **kwargs):
    """
    This method returns a error response which occurs when a resource can't be found.
    """
    return MockResponse(
        status_code=404,
        text="""
    {
        "error": "Resource not found."
    }
    """,
    )


def mock_forbidden(*args, **kwargs):
    """
    This method returns a error response which occurs when a action is forbidden.
    """
    return MockResponse(
        status_code=403,
        text="""
    {
        "message": "Forbidden"
    }
    """,
    )
