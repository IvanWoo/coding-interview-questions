import pytest
from puzzles.partition_labels import partition_labels


def test_partition_labels():
    assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]
