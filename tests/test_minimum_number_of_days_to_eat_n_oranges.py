from puzzles.minimum_number_of_days_to_eat_n_oranges import min_days


def test_min_days():
    assert min_days(1) == 1
    assert min_days(56) == 6
