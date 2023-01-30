import pytest

from puzzles.letter_combinations_of_a_phone_number import letter_combinations


@pytest.mark.parametrize(
    "digits, expected",
    [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
    ],
)
def test_letter_combinations(digits, expected):
    assert sorted(letter_combinations(digits)) == sorted(expected)
