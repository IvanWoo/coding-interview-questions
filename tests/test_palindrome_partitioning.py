import pytest
from puzzles.palindrome_partitioning import partition


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aab", [["aa", "b"], ["a", "a", "b"]]),
        ("a", [["a"]]),
    ],
)
def test_palindrome_partitioning(s, expected):
    assert sorted(partition(s)) == sorted(expected)
