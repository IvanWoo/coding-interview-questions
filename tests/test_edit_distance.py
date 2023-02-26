import pytest

from puzzles.edit_distance import min_distance


@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        ("intention", "execution", 5),
        ("horse", "ros", 3),
        ("", "", 0),
    ],
)
def test_min_distance(word1, word2, expected):
    assert min_distance(word1, word2) == expected
