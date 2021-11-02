from puzzles.count_sorted_vowel_strings import count_vowel_strings


def test_count_vowel_strings():
    assert count_vowel_strings(1) == 5
    assert count_vowel_strings(2) == 15
    assert count_vowel_strings(3) == 35
