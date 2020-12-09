from puzzles.palindrome_pairs import palindrome_pairs


def test_palindrome_pairs():
    assert sorted(palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])) == sorted(
        [
            [0, 1],
            [1, 0],
            [3, 2],
            [2, 4],
        ]
    )
    assert sorted(palindrome_pairs(["bat", "tab", "cat"])) == sorted([[0, 1], [1, 0]])
    assert sorted(palindrome_pairs(["a", ""])) == sorted([[0, 1], [1, 0]])
