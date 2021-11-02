from puzzles.wildcard_matching import is_match


def test_is_match():
    assert is_match("aa", "a") == False
    assert is_match("aa", "*") == True
    assert is_match("cb", "?a") == False
    assert is_match("adceb", "*a*b") == True
    assert is_match("acdcb", "a*c?b") == False
    assert is_match("mississippi", "m??*ss*?i*pi") == False
