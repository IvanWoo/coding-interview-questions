from puzzles.minimum_ascii_delete_sum_for_two_strings import minimum_delete_sum


def test_minimum_delete_sum():
    assert minimum_delete_sum(s1="sea", s2="eat") == 231
    assert minimum_delete_sum(s1="delete", s2="leet") == 403
