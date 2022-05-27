import pytest
from puzzles.number_of_steps_to_reduce_a_number_to_zero import number_of_steps


@pytest.mark.parametrize(
    "num, expected",
    [
        (14, 6),
        (8, 4),
        (123, 12),
    ],
)
def test_number_of_steps(num, expected):
    assert number_of_steps(num) == expected
