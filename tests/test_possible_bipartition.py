import pytest
from puzzles.possible_bipartition import possible_bipartition


@pytest.mark.parametrize(
    "n, dislikes, expected",
    [
        (4, [[1, 2], [1, 3], [2, 4]], True),
        (3, [[1, 2], [1, 3], [2, 3]], False),
        (5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], False),
        (
            10,
            [[5, 9], [5, 10], [5, 6], [5, 7], [1, 5], [4, 5], [2, 5], [5, 8], [3, 5]],
            True,
        ),
    ],
)
def test_possible_bipartition(n, dislikes, expected):
    assert possible_bipartition(n, dislikes) == expected
