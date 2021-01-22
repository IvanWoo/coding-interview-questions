# https://leetcode.com/problems/count-binary-substrings/
"""
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Note:
s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
"""
from functools import lru_cache

# TLE: O(N^2)
def count_binary_substrings(s: str) -> int:
    @lru_cache(None)
    def is_valid(s):
        if not s:
            return 0
        n = len(s)
        if n % 2 != 0:
            return 0
        head, tail = s[0], s[n // 2]
        if head == tail:
            return 0
        for i in range(n // 2):
            if s[i] != head or s[i + n // 2] != tail:
                return 0
        return 1

    res = 0
    n = len(s)
    for i in range(n):
        for j in range(i):
            sub_s = s[j : i + 1]
            if is_valid(sub_s):
                res += 1
    return res


# O(N)
def count_binary_substrings(s: str) -> int:
    res = 0
    n = len(s)
    for i in range(n - 1):
        # find the core then expand
        if s[i] != s[i + 1]:
            left, right = i, i + 1
            res += 1
            while left - 1 >= 0 and right + 1 < n:
                if s[left - 1] == s[left] and s[right] == s[right + 1]:
                    res += 1
                    left -= 1
                    right += 1
                else:
                    break
    return res


if __name__ == "__main__":
    count_binary_substrings("00110011")