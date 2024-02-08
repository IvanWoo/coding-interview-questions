from puzzles.longest_word_in_dictionary import longest_word


def test_longest_word():
    assert longest_word(["w", "wo", "wor", "worl", "world"]) == "world"
    assert (
        longest_word(["a", "banana", "app", "appl", "ap", "apply", "apple"]) == "apple"
    )
