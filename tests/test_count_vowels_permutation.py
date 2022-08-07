import pytest
from puzzles.count_vowels_permutation import count_vowel_permutation


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 5),
        (2, 10),
        (5, 68),
        (144, 18208803),
    ],
)
def test_count_vowel_permutation(n, expected):
    assert count_vowel_permutation(n) == expected
