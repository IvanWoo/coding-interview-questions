import pytest

from puzzles.kth_largest_element_in_a_stream import KthLargest
from tests.utils import assert_obj_outs


@pytest.mark.parametrize(
    "ops, vals, outs",
    [
        (
            [
                "add",
                "add",
                "add",
                "add",
                "add",
            ],
            [[3], [5], [10], [9], [4]],
            [4, 5, 5, 8, 8],
        )
    ],
)
def test_randomized_set(ops, vals, outs):
    obj = KthLargest(3, [4, 5, 8, 2])
    assert_obj_outs(obj, ops, vals, outs)
