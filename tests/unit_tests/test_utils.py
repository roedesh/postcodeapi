from postcodeapi.utils import is_valid_postal_code


def test_is_valid_postal_code():
    assert not is_valid_postal_code("NOT A POSTAL CODE")
    assert is_valid_postal_code("6093BL")
