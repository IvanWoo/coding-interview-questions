# https://leetcode.com/problems/minimum-window-substring/
"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"

Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.
 

Follow up: Could you find an algorithm that runs in O(n) time?
"""
from collections import defaultdict, Counter

# sliding window
def min_window(s: str, t: str) -> str:
    target = Counter(t)
    n = len(s)

    window = defaultdict(int)
    lo, hi = 0, 0
    start = 0
    min_len = float("inf")

    match = 0

    while hi < n:
        c1 = s[hi]
        hi += 1
        if c1 in target.keys():
            window[c1] += 1
            if window[c1] == target[c1]:
                match += 1

        while match == len(target):
            if hi - lo < min_len:
                start = lo
                min_len = hi - lo
            c2 = s[lo]
            lo += 1
            if c2 in target.keys():
                window[c2] -= 1
                if window[c2] < target[c2]:
                    match -= 1
    return s[start : start + min_len] if min_len != float("inf") else ""


if __name__ == "__main__":
    min_window("ADOBECODEBANC", "ABC")
