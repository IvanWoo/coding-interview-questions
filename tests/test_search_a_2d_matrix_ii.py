import pytest
from puzzles.search_a_2d_matrix_ii import search_matrix


@pytest.mark.parametrize(
    "matrix, target, expected",
    [
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            5,
            True,
        ),
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            20,
            False,
        ),
        ([[-5]], -5, True),
        ([[1, 4], [2, 5]], 2, True),
    ],
)
def test_search_matrix(matrix, target, expected):
    assert search_matrix(matrix, target) == expected
