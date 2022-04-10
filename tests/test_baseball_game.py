import pytest
from puzzles.baseball_game import cal_points


@pytest.mark.parametrize(
    "ops, expected",
    [
        (["5", "2", "C", "D", "+"], 30),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
        (["1"], 1),
    ],
)
def test_cal_points(ops: list[str], expected: int):
    assert cal_points(ops) == expected
