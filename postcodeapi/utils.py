import re

DUTCH_POSTAL_CODE_REGEX = re.compile("^[1-9][0-9]{3}\s?[a-zA-Z]{2}$")


def is_valid_postal_code(postal_code):
    return bool(DUTCH_POSTAL_CODE_REGEX.match(postal_code))
