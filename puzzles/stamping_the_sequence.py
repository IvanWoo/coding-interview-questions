# https://leetcode.com/problems/stamping-the-sequence/
"""
You are given two strings stamp and target. Initially, there is a string s of length target.length with all s[i] == '?'.

In one turn, you can place stamp over s and replace every letter in the s with the corresponding letter from stamp.

For example, if stamp = "abc" and target = "abcba", then s is "?????" initially. In one turn you can:
place stamp at index 0 of s to obtain "abc??",
place stamp at index 1 of s to obtain "?abc?", or
place stamp at index 2 of s to obtain "??abc".
Note that stamp must be fully contained in the boundaries of s in order to stamp (i.e., you cannot place stamp at index 3 of s).
We want to convert s to target using at most 10 * target.length turns.

Return an array of the index of the left-most letter being stamped at each turn. If we cannot obtain target from s within 10 * target.length turns, return an empty array.

Example 1:
Input: stamp = "abc", target = "ababc"
Output: [0,2]
Explanation: Initially s = "?????".
- Place stamp at index 0 to get "abc??".
- Place stamp at index 2 to get "ababc".
[1,0,2] would also be accepted as an answer, as well as some other answers.

Example 2:
Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]
Explanation: Initially s = "???????".
- Place stamp at index 3 to get "???abca".
- Place stamp at index 0 to get "abcabca".
- Place stamp at index 1 to get "aabcaca".

Constraints:
1 <= stamp.length <= target.length <= 1000
stamp and target consist of lowercase English letters.
"""


def overwrite(cur: str, idx: int, stamp: str):
    return cur[:idx] + stamp + cur[idx + len(stamp) :]


# brute force: TLE
def moves_to_stamp(stamp: str, target: str) -> list[int]:
    def backtrack(steps: list[int], cur: str):
        nonlocal ans, n
        if ans:
            return
        if len(steps) > 10 * n:
            return
        if cur == target:
            ans = steps[:]
            return
        for i in range(n - len(stamp) + 1):
            if i in steps:
                continue
            steps.append(i)
            new_cur = overwrite(cur, i, stamp)
            backtrack(steps, new_cur)
            steps.pop()

    ans = []
    n = len(target)
    backtrack([], "?" * n)
    return ans


# reverse the process
def moves_to_stamp(stamp: str, target: str) -> list[int]:
    def eq(target: list[str], stamp: str, i: int) -> bool:
        for j, c in enumerate(stamp):
            if not (target[i + j] == c or target[i + j] == "?"):
                return False
        return True

    target = [c for c in target]
    n, m = len(target), len(stamp)
    ans = []
    already_in = set()
    for i in range(n - m + 1):
        if not eq(target, stamp, i):
            continue
        for x in reversed(range(i + 1)):
            if x in already_in:
                break
            already_in.add(x)
            if eq(target, stamp, x):
                ans.append(x)
                target[x : x + m] = "?" * m
    return ans[::-1] if all([c == "?" for c in target]) else []


if __name__ == "__main__":
    moves_to_stamp("abca", "aabcaca")
