from puzzles.longest_substring_with_at_least_k_repeating_characters import longest_substring


def test_longest_substring():
    assert longest_substring("aaabb", 3) == 3
    assert longest_substring("ababbc", 2) == 5
    assert longest_substring("aaabbb", 3) == 6
