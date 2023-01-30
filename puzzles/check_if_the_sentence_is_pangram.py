# https://leetcode.com/problems/check-if-the-sentence-is-pangram/
"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false


Constraints:
1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""


def check_if_pangram(sentence: str) -> bool:
    count = [0] * 26
    for char in sentence:
        count[ord(char) - ord("a")] = 1
    return sum(count) == 26


def check_if_pangram(sentence: str) -> bool:
    return len(set(sentence)) == 26
