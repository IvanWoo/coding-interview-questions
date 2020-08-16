import pytest
from puzzles.increasing_decreasing_string import sort_string


def test_sort_string():
    assert sort_string("aaaabbbbcccc") == "abccbaabccba"
    assert sort_string("rat") == "art"
    assert sort_string("leetcode") == "cdelotee"
    assert sort_string("ggggggg") == "ggggggg"
    assert sort_string("spo") == "ops"
