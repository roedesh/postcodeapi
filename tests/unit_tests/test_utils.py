from postcodeapi.utils import is_valid_postal_code


def test_is_valid_postal_code():
    assert not is_valid_postal_code("NOT A POSTAL CODE")
    assert not is_valid_postal_code("AB1234")
    assert not is_valid_postal_code("ABCD12")
    assert not is_valid_postal_code("123456")
    assert is_valid_postal_code("5038EA")
