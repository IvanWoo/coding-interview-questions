# https://leetcode.com/problems/decode-ways/
"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").


Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""
from functools import cache


# TLE
def num_decodings(s: str) -> int:
    def backtrack(idx: int):
        nonlocal count
        if idx == n:
            count += 1
            return
        if s[idx] == "0":
            return
        backtrack(idx + 1)
        if idx < n - 1:
            if s[idx : idx + 2] <= "26":
                backtrack(idx + 2)

    count = 0
    n = len(s)
    backtrack(0)
    return count


# dp
def num_decodings(s: str) -> int:
    @cache
    def helper(idx: int):
        if idx == n:
            return 1
        if s[idx] == "0":
            return 0
        ans = 0
        ans += helper(idx + 1)
        if idx < n - 1 and s[idx : idx + 2] <= "26":
            ans += helper(idx + 2)
        return ans

    n = len(s)
    return helper(0)


def num_decodings(s: str) -> int:
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = int(s[0] != "0")

    for i in range(2, n + 1):
        if s[i - 1] != "0":
            dp[i] += dp[i - 1]
        if "10" <= s[i - 2 : i] <= "26":
            dp[i] += dp[i - 2]
    return dp[-1]


if __name__ == "__main__":
    num_decodings("226")
