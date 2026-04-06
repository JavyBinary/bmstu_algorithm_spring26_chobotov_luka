from Longest_unique_substring_finder import find_longest_unique_substring


def test_find_longest_unique_substring() -> None:
    assert find_longest_unique_substring("bbbbb") == 1
    assert find_longest_unique_substring("bbab") == 2
    assert find_longest_unique_substring("") == 0
    assert find_longest_unique_substring("abc") == 3
    assert find_longest_unique_substring("baccc") == 3
    assert find_longest_unique_substring(" ") == 1
    assert find_longest_unique_substring("abcdefg") == 7
