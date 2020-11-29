from puzzles.longest_palindromic_subsequence import longest_palindrome_subseq


def test_longest_palindrome_subseq():
    assert longest_palindrome_subseq("bbbab") == 4
    assert longest_palindrome_subseq("babab") == 5
    assert longest_palindrome_subseq("cbbd") == 2
