import pytest
from puzzles.single_threaded_cpu import get_order


@pytest.mark.parametrize(
    "tasks, expected",
    [
        ([[1, 2], [2, 4], [3, 2], [4, 1]], [0, 2, 3, 1]),
        ([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]], [4, 3, 2, 0, 1]),
        ([[5, 2], [7, 2], [9, 4], [6, 3], [5, 10], [1, 1]], [5, 0, 1, 3, 2, 4]),
        (
            [
                [35, 36],
                [11, 7],
                [15, 47],
                [34, 2],
                [47, 19],
                [16, 14],
                [19, 8],
                [7, 34],
                [38, 15],
                [16, 18],
                [27, 22],
                [7, 15],
                [43, 2],
                [10, 5],
                [5, 4],
                [3, 11],
            ],
            [15, 14, 13, 1, 6, 3, 5, 12, 8, 11, 9, 4, 10, 7, 0, 2],
        ),
    ],
)
def test_get_order(tasks, expected):
    assert get_order(tasks) == expected
