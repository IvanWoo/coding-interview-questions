from puzzles.longest_common_subsequence import longest_common_subsequence


def test_longest_common_subsequence():
    assert longest_common_subsequence(text1="abcde", text2="ace") == 3
    assert longest_common_subsequence(text1="abc", text2="abc") == 3
    assert longest_common_subsequence(text1="abc", text2="def") == 0
    assert longest_common_subsequence(text1="bsbininm", text2="jmjkbkjkv") == 1
