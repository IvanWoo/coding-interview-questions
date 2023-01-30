import pytest

from puzzles.my_calendar_iii import MyCalendarThree
from tests.utils import assert_obj_outs


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
    assert_obj_outs(obj, ops, vals, outs)
