import pytest

from puzzles.maximum_value_at_a_given_index_in_a_bounded_array import max_value


@pytest.mark.parametrize(
    "n, index, max_sum, expected",
    [
        (4, 2, 6, 2),
        (6, 1, 10, 3),
    ],
)
def test_max_value(n, index, max_sum, expected):
    assert max_value(n, index, max_sum) == expected
