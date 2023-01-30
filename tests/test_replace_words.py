from puzzles.replace_words import replace_words


def test_replace_words():
    assert (
        replace_words(
            dictionary=["cat", "bat", "rat"],
            sentence="the cattle was rattled by the battery",
        )
        == "the cat was rat by the bat"
    )
    assert (
        replace_words(
            dictionary=["a", "b", "c"], sentence="aadsfasf absbs bbab cadsfafs"
        )
        == "a a b c"
    )
    assert (
        replace_words(
            dictionary=["a", "aa", "aaa", "aaaa"],
            sentence="a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa",
        )
        == "a a a a a a a a bbb baba a"
    )
    assert (
        replace_words(
            dictionary=["catt", "cat", "bat", "rat"],
            sentence="the cattle was rattled by the battery",
        )
        == "the cat was rat by the bat"
    )
    assert (
        replace_words(
            dictionary=["ac", "ab"],
            sentence="it is abnormal that this solution is accepted",
        )
        == "it is ab that this solution is ac"
    )
