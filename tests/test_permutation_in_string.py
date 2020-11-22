from puzzles.permutation_in_string import check_inclusion


def test_check_inclusion():
    assert check_inclusion(s1="ab", s2="eidbaooo") == True
    assert check_inclusion(s1="ab", s2="eidboaoo") == False
    assert check_inclusion(s1="abc", s2="bbbca") == True
