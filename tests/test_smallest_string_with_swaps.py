from puzzles.smallest_string_with_swaps import smallest_string_with_swaps


def test_smallest_string_with_swaps():
    assert smallest_string_with_swaps(s="dcab", pairs=[[0, 3], [1, 2]]) == "bacd"
    assert (
        smallest_string_with_swaps(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]) == "abcd"
    )
    assert smallest_string_with_swaps(s="cba", pairs=[[0, 1], [1, 2]]) == "abc"
