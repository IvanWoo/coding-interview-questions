import pytest

from puzzles.longest_uncommon_subsequence_ii import find_LUS_length


def test_find_LUS_length():
    assert find_LUS_length(["aabbcc", "aabbcc", "cb", "abc"]) == 2
    assert find_LUS_length(["abcabc", "abcabc", "abcabc", "abc", "abc", "bac"]) == -1
    assert find_LUS_length(["abcabc", "abcabc", "abcabc", "abc", "abc", "cca"]) == 3
