import pytest
from puzzles.compare_versions import compare_versions


@pytest.mark.parametrize(
    "version1, version2, expected",
    [
        ("0.1", "1.1", -1),
        ("1.0.1", "1", 1),
        ("7.5.2.4", "7.5.3", -1),
        ("1.01", "1.001", 0),
        ("1.0", "1.0.0", 0),
    ],
)
def test_compare_versions(version1, version2, expected):
    assert compare_versions(version1, version2) == expected
