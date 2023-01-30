import pytest

from puzzles.string_compression_ii import get_length_of_optimal_compression


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("aaabcccd", 2, 4),
        ("aaabcccd", 8, 0),
        ("aabbaa", 2, 2),
        ("aaaaaaaaaaa", 0, 3),
        ("bababbaba", 1, 7),
    ],
)
def test_get_length_of_optimal_compression(s, k, expected):
    assert get_length_of_optimal_compression(s, k) == expected
