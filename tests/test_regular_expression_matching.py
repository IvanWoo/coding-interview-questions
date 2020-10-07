from puzzles.regular_expression_matching import is_match


def test_is_match():
    assert is_match("aa", "a*") == True
    assert is_match("aa", "a") == False
    assert is_match("ab", ".*") == True
    assert is_match("aab", "c*a*b") == True
    assert is_match("mississippi", "mis*is*p*.") == False
