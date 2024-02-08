from puzzles.meeting_rooms import can_attend, minimum_rooms


def test_can_attend():
    assert can_attend([[0, 30], [5, 10], [15, 20]]) == False
    assert can_attend([[7, 10], [2, 4]]) == True
    assert can_attend([[7, 10], [10, 11]]) == True


def test_minimum_rooms():
    assert minimum_rooms([[]]) == 0
    assert minimum_rooms([[0, 30]]) == 1
    assert minimum_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert minimum_rooms([[0, 30], [5, 10], [7, 20]]) == 3
    assert minimum_rooms([[7, 10], [2, 4]]) == 1
    assert minimum_rooms([[7, 10], [10, 11]]) == 1
