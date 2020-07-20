import pytest
from puzzles.compare_versions import compare_versions


def test_compare_versions():
    assert compare_versions("0.1", "1.1") == -1
    assert compare_versions("1.0.1", "1") == 1
    assert compare_versions("7.5.2.4", "7.5.3") == -1
    assert compare_versions("1.01", "1.001") == 0
    assert compare_versions("1.0", "1.0.0") == 0
