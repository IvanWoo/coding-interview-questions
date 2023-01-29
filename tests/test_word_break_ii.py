from puzzles.word_break_ii import word_break


def test_word_break():
    assert sorted(word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"])) == sorted(
        [
            "cats and dog",
            "cat sand dog",
        ]
    )
    assert sorted(word_break("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])) == sorted(
        ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
    )
    assert sorted(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])) == []
