import pytest

from puzzles.most_visited_sector_in_a_circular_track import most_visited


def test_most_visited():
    assert most_visited(4, [1, 3, 1, 2]) == [1, 2]
    assert most_visited(3, [3, 2, 1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 3, 1]) == [1, 3]
