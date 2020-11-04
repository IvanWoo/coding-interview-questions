from puzzles.maximum_length_of_pair_chain import find_longest_chain


def test_find_longest_chain():
    assert find_longest_chain([[1, 2], [2, 3], [3, 4]]) == 2
    assert find_longest_chain([[3, 4], [2, 3], [1, 2]]) == 2
    assert find_longest_chain([[3, 4], [2, 3], [1, 2], [5, 6]]) == 3
    assert find_longest_chain([[3, 4], [2, 3], [1, 2], [5, 6], [3, 5]]) == 3
