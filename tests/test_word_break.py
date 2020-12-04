from puzzles.word_break import word_break


def test_word_break():
    assert word_break("applepenapple", ["apple", "pen", "app"]) == True
    assert word_break("applepenapple", ["apple", "pen"]) == True
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    assert word_break("ab", ["a", "b"]) == True
