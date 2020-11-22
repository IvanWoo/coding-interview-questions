from puzzles.longest_substring_without_repeating_characters import (
    length_of_longest_substring,
)


def test_length_of_longest_substring():
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
