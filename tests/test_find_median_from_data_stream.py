import pytest

from puzzles.find_median_from_data_stream import MedianFinder
from tests.utils import assert_obj_outs


@pytest.mark.parametrize(
    "ops, vals, outs",
    [
        (
            ["addNum", "addNum", "findMedian", "addNum", "findMedian"],
            [[1], [2], [], [3], []],
            [None, None, 1.5, None, 2.0],
        )
    ],
)
def test_median_finder(ops, vals, outs):
    obj = MedianFinder()
    assert_obj_outs(obj, ops, vals, outs)
