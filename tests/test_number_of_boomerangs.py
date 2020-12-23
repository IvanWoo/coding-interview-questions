from puzzles.number_of_boomerangs import number_of_boomerangs


def test_number_of_boomerangs():
    assert number_of_boomerangs([[0, 0], [1, 0], [2, 0]]) == 2
    assert number_of_boomerangs([[1, 1], [2, 2], [3, 3]]) == 2
    assert number_of_boomerangs([[1, 1]]) == 0
