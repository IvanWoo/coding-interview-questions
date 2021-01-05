from puzzles.beautiful_arrangement import count_arrangement


def test_count_arrangement():
    assert count_arrangement(1) == 1
    assert count_arrangement(2) == 2
    assert count_arrangement(3) == 3
