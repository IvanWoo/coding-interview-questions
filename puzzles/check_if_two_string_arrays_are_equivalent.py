# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

Constraints:
1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.
"""


def array_strings_are_equal(word1: list[str], word2: list[str]) -> bool:
    return "".join(word1) == "".join(word2)


def array_strings_are_equal(word1: list[str], word2: list[str]) -> bool:
    def helper(w: list[str]):
        for sub_w in w:
            for char in sub_w:
                yield char
        yield None

    for c1, c2 in zip(helper(word1), helper(word2)):
        if c1 != c2:
            return False
    return True
