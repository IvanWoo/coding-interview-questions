import pytest

from puzzles.binary_trees_with_factors import num_factored_binary_trees


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 4], 3),
        ([2, 5, 10], 5),
        ([2, 4, 5, 10], 7),
        ([18, 3, 6, 2], 12),
        ([15, 13, 22, 7, 11], 5),
    ],
)
def test_num_factored_binary_trees(arr, expected):
    assert num_factored_binary_trees(arr) == expected
