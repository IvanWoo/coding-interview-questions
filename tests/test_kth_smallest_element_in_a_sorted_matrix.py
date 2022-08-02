import pytest
from puzzles.kth_smallest_element_in_a_sorted_matrix import kth_smallest


@pytest.mark.parametrize(
    "matrix, k, expected",
    [
        ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13),
        ([[-5]], 1, -5),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5, 5),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1),
        ([[1, 2], [1, 3]], 2, 1),
        ([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 6, 11),
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            20,
            21,
        ),
    ],
)
def test_kth_smallest(matrix, k, expected):
    assert kth_smallest(matrix, k) == expected
