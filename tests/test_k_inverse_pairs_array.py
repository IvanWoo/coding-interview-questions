import pytest
from puzzles.k_inverse_pairs_array import k_inverse_pairs


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (3, 0, 1),
        (3, 1, 2),
        (3, 2, 2),
        (4, 1, 3),
        (4, 2, 5),
        (100, 20, 997493254),
        (1000, 1000, 663677020),
    ],
)
def test_k_inverse_pairs(n, k, expected):
    assert k_inverse_pairs(n, k) == expected
