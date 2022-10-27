import pytest
from puzzles.image_overlap import largest_overlap


@pytest.mark.parametrize(
    "img1, img2, expected",
    [
        ([[1, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]], 3),
        ([[1]], [[1]], 1),
        ([[0]], [[0]], 0),
        (
            [
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
            ],
            1,
        ),
    ],
)
def test_largest_overlap(img1, img2, expected):
    assert largest_overlap(img1, img2) == expected
