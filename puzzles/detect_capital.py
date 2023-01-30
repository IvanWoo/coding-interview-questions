# https://leetcode.com/problems/detect-capital/description/
"""
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false


Constraints:
1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
"""


def detect_capital_use(word: str) -> bool:
    def all_lower(w):
        return all([ord(c) >= ord("a") for c in w])

    def all_upper(w):
        return all([ord(c) < ord("a") for c in w])

    is_lower = ord(word[0]) >= ord("a")
    if is_lower:
        return all_lower(word[1:])
    else:
        return all_lower(word[1:]) or all_upper(word[1:])


def detect_capital_use(word: str) -> bool:
    return word.isupper() or word.islower() or word.istitle()
