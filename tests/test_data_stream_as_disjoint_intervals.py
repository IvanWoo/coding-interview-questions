import pytest
from puzzles.data_stream_as_disjoint_intervals import SummaryRanges


@pytest.mark.parametrize(
    "ops, vals, outs",
    [
        (
            [
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
            ],
            [[1], [], [3], [], [7], [], [2], [], [6], []],
            [
                None,
                [[1, 1]],
                None,
                [[1, 1], [3, 3]],
                None,
                [[1, 1], [3, 3], [7, 7]],
                None,
                [[1, 3], [7, 7]],
                None,
                [[1, 3], [6, 7]],
            ],
        ),
        (
            [
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
            ],
            [
                [6],
                [],
                [6],
                [],
                [0],
                [],
                [4],
                [],
                [8],
                [],
                [7],
                [],
                [6],
                [],
                [4],
                [],
                [7],
                [],
                [5],
                [],
            ],
            [
                None,
                [[6, 6]],
                None,
                [[6, 6]],
                None,
                [[0, 0], [6, 6]],
                None,
                [[0, 0], [4, 4], [6, 6]],
                None,
                [[0, 0], [4, 4], [6, 6], [8, 8]],
                None,
                [[0, 0], [4, 4], [6, 8]],
                None,
                [[0, 0], [4, 4], [6, 8]],
                None,
                [[0, 0], [4, 4], [6, 8]],
                None,
                [[0, 0], [4, 4], [6, 8]],
                None,
                [[0, 0], [4, 8]],
            ],
        ),
    ],
)
def test_randomized_set(ops, vals, outs):
    obj = SummaryRanges()
    for op, val, out in zip(ops, vals, outs):
        print(f"{op=}, {val=}, {out=}")
        if val != []:
            assert getattr(obj, op)(*val) == out
        else:
            assert getattr(obj, op)() == out
