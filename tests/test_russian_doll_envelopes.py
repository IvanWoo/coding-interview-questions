from puzzles.russian_doll_envelopes import max_envelopes


def test_max_envelopes():
    assert max_envelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3
    assert max_envelopes([[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]]) == 3
