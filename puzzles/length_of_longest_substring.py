# https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def length_of_longest_substring(s: str) -> int:
    longest = 0
    left, right = 0, 0
    chars = set()
    while left < len(s) and right < len(s):
        if s[right] not in chars:
            chars.add(s[right])
            right += 1
            longest = max(longest, right - left)
        else:
            chars.remove(s[left])
            left += 1
    return longest

