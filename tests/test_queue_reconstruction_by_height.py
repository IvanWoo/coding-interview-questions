import pytest
from puzzles.queue_reconstruction_by_height import reconstruct_queue


def test_reconstruct_queue():
    assert reconstruct_queue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]) == [
        [5, 0],
        [7, 0],
        [5, 2],
        [6, 1],
        [4, 4],
        [7, 1],
    ]
