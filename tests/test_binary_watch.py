import pytest
from puzzles.binary_watch import read_binary_watch


def test_read_binary_watch():
    assert read_binary_watch(0) == ["0:00"]
    print(read_binary_watch(1))
    assert sorted(read_binary_watch(1)) == sorted(
        ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
    )
