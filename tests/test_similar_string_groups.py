from puzzles.similar_string_groups import num_similar_groups


def test_num_similar_groups():
    assert num_similar_groups(["tars", "rats", "arts", "star"]) == 2
    assert num_similar_groups(["omv", "ovm"]) == 1
