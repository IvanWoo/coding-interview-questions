# https://leetcode.com/problems/longest-repeating-character-replacement/
"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:
Input:
s = "ABAB", k = 2
Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:
Input:
s = "AABABBA", k = 1
Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""
from collections import Counter


# sliding window
def character_replacement(s: str, k: int) -> int:
    n = len(s)
    left, right = 0, 0
    most = 0
    counter = Counter()
    res = 0
    while right < n:
        right_val = s[right]
        counter[right_val] += 1
        right += 1
        most = max(most, counter[right_val])
        while (right - left) - most > k:
            counter[s[left]] -= 1
            left += 1
            # most = counter.most_common(1)[0][1]
        else:
            res = max(res, right - left)
    return res


if __name__ == "__main__":
    character_replacement("AABABBA", 1)
