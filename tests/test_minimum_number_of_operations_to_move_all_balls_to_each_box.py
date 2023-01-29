from puzzles.minimum_number_of_operations_to_move_all_balls_to_each_box import min_operations


def test_min_operations():
    assert min_operations("110") == [1, 1, 3]
    assert min_operations("001011") == [11, 8, 5, 4, 3, 4]
