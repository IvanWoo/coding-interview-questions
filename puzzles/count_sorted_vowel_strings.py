# https://leetcode.com/problems/count-sorted-vowel-strings/
"""
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

Example 1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:
Input: n = 33
Output: 66045
 
Constraints:

1 <= n <= 50 
"""
from functools import lru_cache

# backtracking
def count_vowel_strings(n: int) -> int:
    count = 0

    def helper(i, l):
        nonlocal count
        if l == n:
            count += 1
            return
        for index in range(i, 5):
            helper(index, l + 1)

    helper(0, 0)
    return count


# top down dp
def count_vowel_strings(n: int) -> int:
    @lru_cache(None)
    def func(n, k):
        if n == 1:
            return k
        return sum(func(n - 1, kk) for kk in range(1, k + 1))

    return func(n, 5)


# dp
def count_vowel_strings(n: int) -> int:
    dp = [[0] * 5 for _ in range(n)]

    for i in range(5):
        dp[0][i] = 1

    for row in range(1, n):
        for col in range(5):
            for pre_col in range(col + 1):
                dp[row][col] += dp[row - 1][pre_col]

    return sum(dp[n - 1])


# dp with space optimization
def count_vowel_strings(n: int) -> int:
    dp = [1] * 5

    for _ in range(1, n):
        new_dp = [0] * 5
        for col in range(5):
            for pre_col in range(col + 1):
                new_dp[col] += dp[pre_col]
        dp = new_dp[:]

    return sum(dp)


def count_vowel_strings(n: int) -> int:
    return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24
