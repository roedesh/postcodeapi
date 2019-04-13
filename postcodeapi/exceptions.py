class NoAccessException(Exception):
    pass


class ResourceNotFoundException(Exception):
    pass


class HouseNumberRequiresPostalCodeException(Exception):
    pass


class InvalidPostalCodeException(Exception):
    pass


class LimitExceededException(Exception):
    pass
