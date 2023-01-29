import pytest

from puzzles.check_if_two_string_arrays_are_equivalent import array_strings_are_equal


@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        (["ab", "c"], ["a", "bc"], True),
        (["a", "cb"], ["ab", "c"], False),
        (["abc", "d", "defg"], ["abcddefg"], True),
        (["abc", "d", "defg"], ["abcddef"], False),
    ],
)
def test_array_strings_are_equal(word1, word2, expected):
    assert array_strings_are_equal(word1, word2) == expected
