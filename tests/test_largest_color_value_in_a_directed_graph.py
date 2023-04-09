import pytest

from puzzles.largest_color_value_in_a_directed_graph import largest_path_value


@pytest.mark.parametrize(
    "colors, edges, expected",
    [
        ("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]], 3),
        ("a", [[0, 0]], -1),
        ("ab", [[0, 1], [1, 1]], -1),
    ],
)
def test_largest_path_value(colors, edges, expected):
    assert largest_path_value(colors, edges) == expected
