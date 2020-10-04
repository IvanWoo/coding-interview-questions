from puzzles.longest_valid_parentheses import longest_valid_parentheses


def test_longest_valid_parentheses():
    assert longest_valid_parentheses("(()") == 2
    assert longest_valid_parentheses(")()())") == 4
    assert longest_valid_parentheses("))))))") == 0
