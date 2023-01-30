from puzzles.task_scheduler import least_interval


def test_least_interval():
    assert least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert least_interval(["A", "A", "B", "C", "D", "E", "F"], 2) == 7
    assert least_interval(["A", "A", "A", "B", "B", "B"], 1) == 6
    assert least_interval(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert (
        least_interval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
        == 16
    )
