import pytest

from puzzles.sign_of_the_product_of_an_array import array_sign


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, -2, -3, -4, 3, 2, 1], 1),
        ([1, 5, 0, 2, -3], 0),
        ([-1, 1, -1, 1, -1], -1),
    ],
)
def test_array_sign(nums, expected):
    assert array_sign(nums) == expected
