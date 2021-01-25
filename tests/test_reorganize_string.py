from puzzles.reorganize_string import reorganize_string


def test_reorganize_string():
    assert reorganize_string("aab") == "aba"
    assert reorganize_string("aaab") == ""
