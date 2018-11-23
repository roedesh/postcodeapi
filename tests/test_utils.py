from postcodeapi.utils import is_valid_dutch_postal_code


def test_is_valid_postal_code():
    assert not is_valid_dutch_postal_code("NOT A POSTAL CODE")
    assert is_valid_dutch_postal_code("6093BL")
    assert is_valid_dutch_postal_code("6093bl")
    assert is_valid_dutch_postal_code("6093 BL")
    assert not is_valid_dutch_postal_code("6093sa")
    assert not is_valid_dutch_postal_code("6093SA")
    assert not is_valid_dutch_postal_code("6093sd")
    assert not is_valid_dutch_postal_code("6093SD")
    assert not is_valid_dutch_postal_code("6093ss")
    assert not is_valid_dutch_postal_code("6093SS")
