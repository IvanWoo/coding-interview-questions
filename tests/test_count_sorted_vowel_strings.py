import pytest

from puzzles.count_sorted_vowel_strings import count_vowel_strings


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 5),
        (2, 15),
        (3, 35),
        (33, 66045),
    ],
)
def test_count_vowel_strings(n, expected):
    assert count_vowel_strings(n) == expected
