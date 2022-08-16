# https://leetcode.com/problems/first-unique-character-in-a-string/
"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
"""
from collections import Counter, defaultdict, deque


def first_uniq_char(s: str) -> int:
    c = Counter(s)
    for i, char in enumerate(s):
        if c[char] == 1:
            return i
    return -1


def first_uniq_char(s: str) -> int:
    counter = defaultdict(int)
    q = deque()
    for i, char in enumerate(s):
        counter[char] += 1
        if counter[char] == 1:
            q.append((char, i))
        while q and counter[q[0][0]] > 1:
            q.popleft()
    return -1 if not q else q[0][1]
