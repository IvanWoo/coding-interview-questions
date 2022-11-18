import pytest
from puzzles.ugly_number import is_ugly


@pytest.mark.parametrize(
    "n, expected",
    [
        (6, True),
        (1, True),
        (-1, False),
        (14, False),
    ],
)
def test_is_ugly(n, expected):
    assert is_ugly(n) == expected
