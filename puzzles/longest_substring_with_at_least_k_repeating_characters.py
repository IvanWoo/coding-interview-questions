# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
"""
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Constraints:
1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
"""
from collections import Counter, defaultdict

# TLE: O(N^3)
def longest_substring(s: str, k: int) -> int:
    res = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            if (j - i + 1) <= res:
                continue
            c = Counter(s[i : j + 1])
            if all([v >= k for _, v in c.items()]):
                res = max(res, j - i + 1)
    return res


# sliding windows: O(N)
def longest_substring(s: str, k: int) -> int:
    n = len(s)
    res = 0
    for t in range(1, len(Counter(s)) + 1):
        start, end = 0, 0
        freq = [0] * 26
        unique, meet = 0, 0
        while end < n:
            if unique <= t:
                char_new = ord(s[end]) - ord("a")
                freq[char_new] += 1
                if freq[char_new] == 1:
                    unique += 1
                if freq[char_new] == k:
                    meet += 1
                end += 1
            else:
                char_start = ord(s[start]) - ord("a")
                start += 1
                if freq[char_start] == k:
                    meet -= 1
                freq[char_start] -= 1
                if freq[char_start] == 0:
                    unique -= 1

            if unique == t and meet == t:
                res = max(res, end - start)
    return res


if __name__ == "__main__":
    longest_substring("aaabb", 3)