# https://leetcode.com/problems/count-vowels-permutation/
"""
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

Example 2:
Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

Example 3:
Input: n = 5
Output: 68


Constraints:
1 <= n <= 2 * 10^4
"""


def count_vowel_permutation(n: int) -> int:
    def generate_rules():
        nxt = {
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"],
        }

        rules = [None] * 5
        VOWELS = "aeiou"
        for i, char in enumerate(VOWELS):
            rules[i] = [VOWELS.index(c) for c in nxt[char]]
        return rules

    rules = generate_rules()
    MOD = 10**9 + 7
    dp = [[0 for _ in range(5)] for _ in range(n)]
    for i in range(5):
        dp[0][i] = 1

    for row in range(1, n):
        for i in range(5):
            for nxt in rules[i]:
                dp[row][nxt] += dp[row - 1][i]

    return sum(dp[-1]) % MOD


# compression the states
def count_vowel_permutation(n: int) -> int:
    MOD = 10**9 + 7
    a, e, i, o, u = 1, 1, 1, 1, 1
    for _ in range(n - 1):
        a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
    return (a + e + i + o + u) % MOD
