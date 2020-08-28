import pytest
from puzzles.palindrome_permutation import palindrome_permutation


def test_palindrome_permutation():
    assert palindrome_permutation("aabb") == sorted(["abba", "baab"])
    assert palindrome_permutation("aaaabbbb") == sorted(
        [
            "aabbbbaa",
            "bbaaaabb",
            "ababbaba",
            "babaabab",
            "abbaabba",
            "baabbaab",
        ]
    )
    assert palindrome_permutation("aab") == ["aba"]
    assert palindrome_permutation("aaa") == ["aaa"]
    assert palindrome_permutation("aaab") == []
    assert palindrome_permutation("abc") == []
    assert palindrome_permutation("aaabbb") == []
