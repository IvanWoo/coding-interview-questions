from puzzles.count_binary_substrings import count_binary_substrings


def test_count_binary_substrings():
    assert count_binary_substrings("00110") == 3
    assert count_binary_substrings("00110011") == 6
    assert count_binary_substrings("10101") == 4
