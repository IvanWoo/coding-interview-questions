import pytest

from puzzles.linked_list_random_node import Solution
from puzzles.utils import make_linked_list


@pytest.mark.parametrize(
    "head, expected",
    [
        (
            make_linked_list([1, 2, 3]),
            [1, 2, 3],
        )
    ],
)
def test_solution(head, expected):
    instance = Solution(head)
    for _ in range(5):
        assert instance.get_random() in expected
