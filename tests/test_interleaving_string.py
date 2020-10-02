from puzzles.interleaving_string import is_interleave


def test_is_interleave():
    assert is_interleave("aabcc", "dbbca", "aadbbcbcac") == True
    assert is_interleave("", "", "") == True
    assert is_interleave("aabcc", "dbbca", "aadbbbaccc") == False
