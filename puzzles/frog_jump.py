# https://leetcode.com/problems/frog-jump/
"""
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.

Example 1:
[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.

Example 2:
[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.
"""
from typing import List


# TLE
def can_cross(stones: List[int]) -> bool:
    n = len(stones)
    dp = [None] * n
    dp[0] = set([0])
    for i in range(1, n):
        new_steps = set([])
        for j in range(i):
            if not dp[j]:
                continue
            for k in dp[j]:
                if stones[i] - stones[j] in [k - 1, k, k + 1]:
                    new_steps.add(stones[i] - stones[j])
        if new_steps:
            dp[i] = new_steps
    return dp[-1] is not None


def can_cross(stones: List[int]) -> bool:
    n = len(stones)
    # dp[i][j] denote at stone i, the frog can or cannot make jump of size j
    dp = [[False] * (n + 1) for _ in range(n)]
    dp[0][1] = True
    for i in range(1, n):
        for j in range(i):
            diff = stones[i] - stones[j]
            if diff < 0 or diff > n or not dp[j][diff]:
                continue
            dp[i][diff] = True
            if diff - 1 >= 0:
                dp[i][diff - 1] = True
            if diff + 1 <= n:
                dp[i][diff + 1] = True
            if i == n - 1:
                return True
    return False


if __name__ == "__main__":
    can_cross([0, 1, 3, 5, 6, 8, 12, 16, 18])
