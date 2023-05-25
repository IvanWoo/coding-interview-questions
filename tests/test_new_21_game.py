import pytest

from puzzles.new_21_game import new_21_game


@pytest.mark.parametrize(
    "n, k, max_pts, expected",
    [
        (10, 1, 10, 1),
        (6, 1, 10, 0.6),
        (21, 17, 10, 0.73278),
    ],
)
def test_new_21_game(n, k, max_pts, expected):
    assert new_21_game(n, k, max_pts) == pytest.approx(expected, rel=1e-5)
