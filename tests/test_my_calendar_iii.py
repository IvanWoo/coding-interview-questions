import pytest
from puzzles.my_calendar_iii import MyCalendarThree


@pytest.mark.parametrize(
    "ops, vals, outs",
    [
        (
            ["book", "book", "book", "book", "book", "book"],
            [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
            [1, 1, 2, 3, 3, 3],
        )
    ],
)
def test_my_calendar_three(ops, vals, outs):
    obj = MyCalendarThree()
    for op, val, out in zip(ops, vals, outs):
        print(f"{op=}")
        print(f"{val=}")
        print(f"{out=}")
        assert getattr(obj, op)(*val) == out
