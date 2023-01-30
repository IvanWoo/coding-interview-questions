import pytest

from puzzles.cheapest_flights_within_k_stops import find_cheapest_price


@pytest.mark.parametrize(
    "n, flights, src, dst, k, expected",
    [
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500),
        (
            5,
            [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]],
            2,
            1,
            1,
            -1,
        ),
        (4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1, 6),
    ],
)
def test_find_cheapest_price(n, flights, src, dst, k, expected):
    assert find_cheapest_price(n, flights, src, dst, k) == expected
