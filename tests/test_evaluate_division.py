import pytest

from puzzles.evaluate_division import calc_equation


@pytest.mark.parametrize(
    "equations, values, queries, expected",
    [
        (
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            [6.0, 0.5, -1, 1, -1],
        ),
        (
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            [3.75, 0.4, 5.0, 0.2],
        ),
        (
            [["a", "b"]],
            [0.5],
            [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
            [0.5, 2, -1, -1],
        ),
    ],
)
def test_calc_equation(equations, values, queries, expected):
    assert calc_equation(equations, values, queries) == expected
