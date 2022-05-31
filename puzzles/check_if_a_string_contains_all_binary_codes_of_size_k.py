# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
"""
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

Example 1:
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.

Example 2:
Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 

Example 3:
Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.

Constraints:
1 <= s.length <= 5 * 105
s[i] is either '0' or '1'.
1 <= k <= 20
"""


def has_all_codes(s: str, k: int) -> bool:
    total = 1 << k
    bucket = {k: False for k in range(total)}
    n = len(s)
    for i in range(n - k + 1):
        char = s[i : i + k]
        bucket[int(char, 2)] = True

    for i in range(total):
        if not bucket[i]:
            return False
    return True


def has_all_codes(s: str, k: int) -> bool:
    return len(set(s[i : i + k] for i in range(len(s) - k + 1))) == (1 << k)


if __name__ == "__main__":
    has_all_codes("00110", 2)
