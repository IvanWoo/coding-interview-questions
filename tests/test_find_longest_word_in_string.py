import pytest
from puzzles.find_longest_word_in_string import find_longest_word_in_string


def test_find_longest_word_in_string():
    assert (
        find_longest_word_in_string(
            "abppplee", {"able", "ale", "apple", "bale", "kangaroo"}
        )
        == "apple"
    )

    assert (
        find_longest_word_in_string(
            "abppplee", {"able", "ale", "apple", "bale", "kangaroo", "ppplee"}
        )
        == "ppplee"
    )
