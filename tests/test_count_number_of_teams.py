from puzzles.count_number_of_teams import num_teams


def test_num_teams():
    assert num_teams([2, 5, 3, 4, 1]) == 3
    assert num_teams([2, 1, 3]) == 0
    assert num_teams([1, 2, 3, 4]) == 4
    assert num_teams([1, 2]) == 0
    assert num_teams([]) == 0
