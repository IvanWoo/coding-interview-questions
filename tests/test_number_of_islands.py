import pytest
from puzzles.number_of_islands import num_islands


def test_num_islands():
    assert (
        num_islands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )
    assert (
        num_islands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )
