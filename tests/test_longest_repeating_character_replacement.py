from puzzles.longest_repeating_character_replacement import character_replacement


def test_character_replacement():
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
