from puzzles.minimum_window_substring import min_window


def test_min_window():
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
