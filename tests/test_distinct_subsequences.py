from puzzles.distinct_subsequences import num_distinct


def test_num_distinct():
    assert num_distinct(s="rabbbit", t="rabbit") == 3
    assert num_distinct(s="babgbag", t="bag") == 5
