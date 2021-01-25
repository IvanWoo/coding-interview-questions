# https://leetcode.com/problems/reorganize-string/
"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:
Input: S = "aab"
Output: "aba"

Example 2:
Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
from collections import Counter


def reorganize_string(S: str) -> str:
    n = len(S)
    counter = Counter(S)
    most_common_char = counter.most_common(1)[0][0]
    if 2 * counter[most_common_char] - 1 > n:
        return ""

    counter[most_common_char] -= 1
    res = most_common_char
    while len(res) != n:
        for c, f in counter.most_common(501):
            if f > 0 and c != res[-1]:
                res += c
                counter[c] -= 1
                break
    return res


if __name__ == "__main__":
    reorganize_string("aab")
