import pytest
from puzzles.insert_delete_getrandom import RandomizedSet


@pytest.mark.parametrize(
    "ops, vals, outs",
    [
        (
            [
                "insert",
                "remove",
                "insert",
                "getRandom",
                "remove",
                "insert",
                "getRandom",
            ],
            [[1], [2], [2], [], [1], [2], []],
            [True, False, True, 2, True, False, 2],
        )
    ],
)
def test_randomized_set(ops, vals, outs):
    obj = RandomizedSet()
    for op, val, out in zip(ops, vals, outs):
        if val != []:
            assert getattr(obj, op)(*val) == out
