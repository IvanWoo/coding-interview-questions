import pytest

from puzzles.minimum_flips_to_make_a_or_b_equal_to_c import min_flips


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (2, 6, 5, 3),
        (4, 2, 7, 1),
        (1, 2, 3, 0),
    ],
)
def test_min_flips(a, b, c, expected):
    assert min_flips(a, b, c) == expected
