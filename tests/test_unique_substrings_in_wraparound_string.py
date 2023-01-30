from puzzles.unique_substrings_in_wraparound_string import (
    find_substring_in_wrapround_string,
)


def test_find_substring_in_wrapround_string():
    assert find_substring_in_wrapround_string("a") == 1
    assert find_substring_in_wrapround_string("cac") == 2
    assert find_substring_in_wrapround_string("zab") == 6
