import pytest
from puzzles.count_and_say import count_and_say


def test_count_and_say():
    assert count_and_say(1) == "1"
    assert count_and_say(2) == "11"
    assert count_and_say(3) == "21"
    assert count_and_say(4) == "1211"
    assert count_and_say(5) == "111221"
    assert count_and_say(6) == "312211"
