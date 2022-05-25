# https://leetcode.com/problems/russian-doll-envelopes/
"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""
from bisect import bisect_left


# patience sorting
def max_envelopes(envelopes: list[list[int]]) -> int:
    # sort envelopes and regress into a LIS problem
    sorted_envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))

    sub = []
    for _, h in sorted_envelopes:
        i = bisect_left(sub, h)
        if i == len(sub):
            sub.append(h)
        else:
            sub[i] = h
    return len(sub)


# brute force: TLE
def max_envelopes(envelopes: list[list[int]]) -> int:
    def can_inside(i, j):
        wi, hi = envelopes[i]
        wj, hj = envelopes[j]
        return wi < wj and hi < hj

    def dfs(path):
        nonlocal res, n
        res = max(res, len(path))

        last = path[-1]
        for j in range(n):
            if j in path:
                continue
            if can_inside(last, j):
                dfs(path + [j])

    n = len(envelopes)
    res = 0
    for i in range(n):
        dfs([i])

    return res


# dp: TLE
def max_envelopes(envelopes: list[list[int]]) -> int:
    def can_inside(i, j):
        wi, hi = envelopes[i]
        wj, hj = envelopes[j]
        return wi < wj and hi < hj

    envelopes.sort()
    n = len(envelopes)
    dp = [1] * n
    for i in range(1, n):
        candidates = [v for k, v in enumerate(dp[:i]) if can_inside(k, i)]
        if candidates:
            dp[i] = max(candidates) + 1

    return max(dp)


if __name__ == "__main__":
    max_envelopes([[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]])
