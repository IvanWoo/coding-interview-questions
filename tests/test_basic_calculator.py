from puzzles.basic_calculator import calculate


def test_calculate():
    assert calculate("-2") == -2
    assert calculate("42") == 42
    assert calculate("1 + 1") == 2
    assert calculate(" 1+1") == 2
    assert calculate(" 2-1 + 2 ") == 3
    assert calculate("(6+8)") == 14
    assert calculate("(4+5- 2)") == 7
    assert calculate("1+(4+5+2)-3") == 9
    assert calculate("(1+(4+5+2)-3)") == 9
    assert calculate("(1+(4+5+2)-3)+(6+8)") == 23
