from puzzles.find_all_anagrams_in_a_string import find_anagrams


def test_find_anagrams():
    assert find_anagrams("cbaebabacd", "abc") == [0, 6]
    assert find_anagrams("abab", "ab") == [0, 1, 2]
    assert find_anagrams("baa", "aa") == [1]
