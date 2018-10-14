class NoAccess(Exception):
    """
    This exception will be raised when a request is made which is not allowed.
    """

    def __init__(self):
        super().__init__("The current account is not allowed to do this")


class ResourceNotFound(Exception):
    """
    This exception will be raised when a requested object cannot be found.
    """

    def __init__(self):
        super().__init__("Object not found")


class HouseNumberRequiresPostalCode(Exception):
    """
    This exception will be raised when attempting to filter on a house number without providing a postal code.
    """

    def __init__(self):
        super().__init__("Filtering on a house number requires a postal code")


class InvalidPostalCode(Exception):
    """
    This exception will be raised when the user provides a value that doesn't pass the Dutch postal code regex.
    """

    def __init__(self):
        super().__init__("The given postal code is invalid")
