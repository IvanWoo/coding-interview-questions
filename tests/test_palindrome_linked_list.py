import pytest
from puzzles.utils import make_linked_list
from puzzles.palindrome_linked_list import is_palindrome


@pytest.mark.parametrize(
    "head, expected",
    [
        (make_linked_list([1, 2, 2, 1]), True),
        (make_linked_list([1, 2]), False),
    ],
)
def test_is_palindrome(head, expected):
    assert is_palindrome(head) == expected
