from puzzles.remove_invalid_parentheses import remove_invalid_parentheses


def test_remove_invalid_parentheses():
    assert sorted(remove_invalid_parentheses("()())()")) == sorted(["()()()", "(())()"])
    assert sorted(remove_invalid_parentheses("(a)())()")) == sorted(
        ["(a)()()", "(a())()"]
    )
    assert remove_invalid_parentheses(")(") == [""]
    assert remove_invalid_parentheses(")a(") == ["a"]
