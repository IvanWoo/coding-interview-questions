import pytest
from puzzles.find_median_from_data_stream import MedianFinder


@pytest.mark.parametrize(
    "ops, nums, outs",
    [
        (
            ["addNum", "addNum", "findMedian", "addNum", "findMedian"],
            [[1], [2], [], [3], []],
            [None, None, 1.5, None, 2.0],
        )
    ],
)
def test_median_finder(ops, nums, outs):
    obj = MedianFinder()
    for op, num, out in zip(ops, nums, outs):
        print(f"{op=}")
        print(f"{num=}")
        print(f"{out=}")
        assert getattr(obj, op)(*num) == out
