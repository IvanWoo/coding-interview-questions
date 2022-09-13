import pytest
from puzzles.utf_8_validation import valid_utf8


@pytest.mark.parametrize(
    "data, expected",
    [
        ([197, 130, 1], True),
        ([235, 140, 4], False),
        ([255, 255], False),
        ([255], False),
    ],
)
def test_valid_utf8(data, expected):
    assert valid_utf8(data) == expected
