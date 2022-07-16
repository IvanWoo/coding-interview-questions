import pytest
from puzzles.utils import make_linked_list
from puzzles.reverse_linked_list import reverse_list


@pytest.mark.parametrize(
    "head, ans",
    [
        (make_linked_list([1, 2, 3, 4, 5]), make_linked_list([5, 4, 3, 2, 1])),
        (make_linked_list([1, 2, 3, 4]), make_linked_list([4, 3, 2, 1])),
    ],
)
def test_reverse_list(head, ans):
    assert reverse_list(head) == ans
