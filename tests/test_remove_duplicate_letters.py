from puzzles.remove_duplicate_letters import remove_duplicate_letters


def test_remove_duplicate_letters():
    assert remove_duplicate_letters("bcabc") == "abc"
    assert remove_duplicate_letters("cbacdcbc") == "acdb"
