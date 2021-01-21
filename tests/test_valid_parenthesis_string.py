from puzzles.valid_parenthesis_string import check_valid_string


def test_check_valid_string():
    assert check_valid_string("*()") == True
    assert check_valid_string("((*)") == True
    assert check_valid_string("()") == True
    assert check_valid_string("()()") == True
    assert check_valid_string("(*)") == True
    assert check_valid_string("(*))") == True
    assert check_valid_string(")*)(") == False
    assert (
        check_valid_string("*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)")
        == False
    )
    assert (
        check_valid_string("((()))()(())(*()()())**(())()()()()((*()*))((*()*)") == True
    )
