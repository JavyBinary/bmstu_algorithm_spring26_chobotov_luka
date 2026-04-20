from K_largest_element import find_k_largest_element


def test_find_k_largest_element() -> None:
    assert find_k_largest_element([3, 2, 1, 6, 5, 4], 2) == 5
    assert find_k_largest_element([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_k_largest_element([], 2) == -1
    assert find_k_largest_element([1, 2, 3], 5) == -1
