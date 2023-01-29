from puzzles.largest_substring_between_two_equal_characters import max_length_between_equal_characters


def test_max_length_between_equal_characters():
    assert max_length_between_equal_characters("aa") == 0
    assert max_length_between_equal_characters("a") == -1
    assert max_length_between_equal_characters("abca") == 2
    assert max_length_between_equal_characters("cbzxy") == -1
    assert max_length_between_equal_characters("cabbac") == 4
