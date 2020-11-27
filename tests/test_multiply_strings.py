from puzzles.multiply_strings import multiply


def test_multiply():
    assert multiply("2", "3") == "6"
    assert multiply("123", "456") == "56088"
