# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
"""
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.

Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
"""


# brute force: O(2^n)
def max_length(arr: list[str]) -> int:
    def is_unique(s: str) -> bool:
        return len(s) == len(set(s))

    def backtrack(idx: int, cur: str):
        nonlocal ans
        if not is_unique(cur):
            return
        ans = max(ans, len(cur))
        if idx >= len(arr):
            return
        backtrack(idx + 1, cur + arr[idx])
        backtrack(idx + 1, cur)

    ans = 0
    backtrack(0, "")
    return ans
