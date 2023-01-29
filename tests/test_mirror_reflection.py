import pytest

from puzzles.mirror_reflection import mirror_reflection


@pytest.mark.parametrize(
    "p, q, expected",
    [
        (2, 1, 2),
        (3, 1, 1),
    ],
)
def test_mirror_reflection(p, q, expected):
    assert mirror_reflection(p, q) == expected
