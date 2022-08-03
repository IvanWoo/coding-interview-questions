from puzzles.my_calendar_i import MyCalendar


def test_my_calendar():
    my_calendar = MyCalendar()
    for start, end, expected in [
        (10, 20, True),
        (15, 25, False),
        (20, 30, True),
    ]:
        assert my_calendar.book(start, end) == expected
