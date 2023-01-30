import pytest

from puzzles.russian_doll_envelopes import max_envelopes


@pytest.mark.parametrize(
    "envelopes, expected",
    [
        ([[1, 1], [1, 1], [1, 1]], 1),
        ([[5, 4], [6, 4], [6, 7], [2, 3]], 3),
        ([[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]], 3),
    ],
)
def test_max_envelopes(envelopes, expected):
    assert max_envelopes(envelopes) == expected
