from puzzles.min_cost_to_connect_all_points import min_cost_connect_points


def test_min_cost_connect_points():
    assert min_cost_connect_points([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert min_cost_connect_points([[3, 12], [-2, 5], [-4, 1]]) == 18
    assert min_cost_connect_points([[0, 0], [1, 1], [1, 0], [-1, 1]]) == 4
    assert (
        min_cost_connect_points([[-1000000, -1000000], [1000000, 1000000]]) == 4000000
    )
    assert min_cost_connect_points([[0, 0]]) == 0
