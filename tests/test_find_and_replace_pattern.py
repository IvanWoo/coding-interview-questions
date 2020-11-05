from puzzles.find_and_replace_pattern import find_and_replace_pattern


def test_find_and_replace_pattern():
    assert find_and_replace_pattern(
        ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"
    ) == ["mee", "aqq"]
