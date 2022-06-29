import pytest
from puzzles.queue_reconstruction_by_height import reconstruct_queue


@pytest.mark.parametrize(
    "people, expected",
    [
        (
            [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
            [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
        ),
        (
            [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]],
            [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]],
        ),
    ],
)
def test_reconstruct_queue(people, expected):
    assert reconstruct_queue(people) == expected
