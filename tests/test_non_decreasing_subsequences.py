import pytest

from puzzles.non_decreasing_subsequences import find_subsequences


@pytest.mark.parametrize(
    "nums, expected",
    [
        (
            [4, 6, 7, 7],
            [
                [4, 6],
                [4, 6, 7],
                [4, 6, 7, 7],
                [4, 7],
                [4, 7, 7],
                [6, 7],
                [6, 7, 7],
                [7, 7],
            ],
        ),
        ([4, 4, 3, 2, 1], [[4, 4]]),
    ],
)
def test_find_subsequences(nums, expected):
    assert sorted(find_subsequences(nums)) == sorted(expected)
