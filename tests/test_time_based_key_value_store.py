import pytest
from puzzles.time_based_key_value_store import TimeMap


@pytest.mark.parametrize(
    "ops, vals, outs",
    [
        (["set"], [["foo", "bar", 1]], [None]),
        (
            ["set", "get", "get", "set", "get", "get"],
            [
                ["foo", "bar", 1],
                ["foo", 1],
                ["foo", 3],
                ["foo", "bar2", 4],
                ["foo", 4],
                ["foo", 5],
            ],
            [None, "bar", "bar", None, "bar2", "bar2"],
        ),
        (
            ["set", "set", "get", "get", "get", "get", "get"],
            [
                ["love", "high", 10],
                ["love", "low", 20],
                ["love", 5],
                ["love", 10],
                ["love", 15],
                ["love", 20],
                ["love", 25],
            ],
            [None, None, "", "high", "high", "low", "low"],
        ),
    ],
)
def test_timemap(ops, vals, outs):
    obj = TimeMap()
    for op, val, out in zip(ops, vals, outs):
        print(f"{op=}")
        print(f"{val=}")
        print(f"{out=}")
        assert getattr(obj, op)(*val) == out
