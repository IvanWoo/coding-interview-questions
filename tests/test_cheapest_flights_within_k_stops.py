from puzzles.cheapest_flights_within_k_stops import find_cheapest_price


def test_find_cheapest_price():
    assert (
        find_cheapest_price(
            n=3, edges=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1
        )
        == 200
    )
    assert (
        find_cheapest_price(
            n=3, edges=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0
        )
        == 500
    )
    assert (
        find_cheapest_price(
            n=5,
            edges=[[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]],
            src=2,
            dst=1,
            k=1,
        )
        == -1
    )
    assert (
        find_cheapest_price(
            n=4,
            edges=[[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]],
            src=0,
            dst=3,
            k=1,
        )
        == 6
    )
