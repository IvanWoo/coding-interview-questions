import pytest

from puzzles.number_of_1_bits import hamming_weight


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 1),
        (5, 2),
    ],
)
def test_hamming_weight(n, expected):
    assert hamming_weight(n) == expected
