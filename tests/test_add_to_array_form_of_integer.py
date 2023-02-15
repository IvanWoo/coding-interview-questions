import pytest

from puzzles.add_to_array_form_of_integer import add_to_array_form


@pytest.mark.parametrize(
    "num, k, expected",
    [
        ([1, 2, 0, 0], 34, [1, 2, 3, 4]),
        ([2, 7, 4], 181, [4, 5, 5]),
        ([2, 1, 5], 806, [1, 0, 2, 1]),
    ],
)
def test_add_to_array_form(num, k, expected):
    assert add_to_array_form(num, k) == expected
