import pytest

from puzzles.unique_paths import unique_paths


@pytest.mark.parametrize(
    "m, n, expected",
    [
        (3, 2, 3),
        (7, 3, 28),
        (1, 1, 1),
    ],
)
def test_unique_paths(m, n, expected):
    assert unique_paths(m, n) == expected
