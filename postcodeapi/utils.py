import re

DUTCH_POSTAL_CODE_REGEX = re.compile(
    "^[1-9][0-9]{3} ?(?!sa|SA|sd|SD|ss|SS)[a-zA-Z]{2}$"
)


def is_valid_dutch_postal_code(postal_code):
    """
    Checks if the given postal code matches the Dutch postal code regex.

    :param postal_code: Dutch postal code
    :return: True if it's a match, else False
    """
    return bool(DUTCH_POSTAL_CODE_REGEX.match(postal_code))
