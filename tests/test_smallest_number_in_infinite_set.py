import pytest

from puzzles.smallest_number_in_infinite_set import SmallestInfiniteSet
from tests.utils import assert_obj_outs


@pytest.mark.parametrize(
    "ops, vals, outs",
    [
        (
            [
                "addBack",
                "popSmallest",
                "popSmallest",
                "popSmallest",
                "addBack",
                "popSmallest",
                "popSmallest",
                "popSmallest",
            ],
            [[2], [], [], [], [1], [], [], []],
            [None, 1, 2, 3, None, 1, 4, 5],
        )
    ],
)
def test_smallest_infinite_set(ops, vals, outs):
    obj = SmallestInfiniteSet()
    assert_obj_outs(obj, ops, vals, outs)
