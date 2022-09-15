import pytest
from puzzles.find_original_array_from_doubled_array import find_original_array


@pytest.mark.parametrize(
    "changed, expected",
    [
        ([1, 3, 4, 2, 6, 8], [1, 3, 4]),
        ([6, 3, 0, 1], []),
        ([1], []),
        ([2, 1], [1]),
        ([0, 0, 0, 0], [0, 0]),
    ],
)
def test_find_original_array(changed, expected):
    assert find_original_array(changed) == expected
