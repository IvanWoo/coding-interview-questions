import pytest
from puzzles.container_with_most_water import max_area


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([1, 2, 3, 4, 5], 4),
        ([1, 2, 5, 8, 7], 7),
    ],
)
def test_max_area(height, expected):
    assert max_area(height) == expected
