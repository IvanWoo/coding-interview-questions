import pytest

from puzzles.number_of_dice_rolls_with_target_sum import num_rolls_to_target


@pytest.mark.parametrize("n, k, target, expected", [(1, 6, 3, 1), (2, 6, 7, 6), (30, 30, 500, 222616187)])
def test_num_rolls_to_target(n, k, target, expected):
    assert num_rolls_to_target(n, k, target) == expected
