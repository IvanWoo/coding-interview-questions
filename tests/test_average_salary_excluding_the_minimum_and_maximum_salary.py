import pytest

from puzzles.average_salary_excluding_the_minimum_and_maximum_salary import average


@pytest.mark.parametrize(
    "salary, expected",
    [
        ([4000, 3000, 1000, 2000], 2500.00000),
        ([1000, 2000, 3000], 2000.00000),
    ],
)
def test_average(salary, expected):
    assert average(salary) == expected
