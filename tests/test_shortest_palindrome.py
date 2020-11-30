from puzzles.shortest_palindrome import shortest_palindrome


def test_shortest_palindrome():
    assert shortest_palindrome("aacecaaa") == "aaacecaaa"
    assert shortest_palindrome("") == ""
    assert shortest_palindrome("abcd") == "dcbabcd"
    assert shortest_palindrome("abbacd") == "dcabbacd"
