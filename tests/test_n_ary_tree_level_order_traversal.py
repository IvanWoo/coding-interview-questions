import pytest

from puzzles.n_ary_tree_level_order_traversal import level_order
from puzzles.utils import make_nary_node


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_nary_node([1, None, 3, 2, 4, None, 5, 6]), [[1], [3, 2, 4], [5, 6]]),
        (
            make_nary_node(
                [
                    1,
                    None,
                    2,
                    3,
                    4,
                    5,
                    None,
                    None,
                    6,
                    7,
                    None,
                    8,
                    None,
                    9,
                    10,
                    None,
                    None,
                    11,
                    None,
                    12,
                    None,
                    13,
                    None,
                    None,
                    14,
                ]
            ),
            [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]],
        ),
    ],
)
def test_level_order(root, expected):
    assert level_order(root) == expected
