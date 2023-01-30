# https://leetcode.com/problems/last-stone-weight-ii/
"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.

Example 2:
Input: stones = [31,26,33,21,40]
Output: 5

Example 3:
Input: stones = [1,2]
Output: 1

Constraints:
1 <= stones.length <= 30
1 <= stones[i] <= 100
"""


def last_stone_weight_ii(stones: list[int]) -> int:
    def knapsack(stones, capacity):
        n = len(stones)
        dp = [[0] * (capacity + 1) for _ in range(n)]

        # init
        # b/c the weights and values are identical in this case
        # we can safely ignore this part
        for j in range(capacity + 1):
            if stones[0] <= j:
                dp[0][j] = stones[0]

        for i, stone in enumerate(stones):
            for j in range(capacity + 1):
                if j < stone:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stone] + stone)
        return dp[-1][-1]

    total = sum(stones)
    # the other subsets: total - knapsack(stones, total // 2)
    # diff: (total - knapsack(stones, total // 2)) - knapsack(stones, total // 2)
    # simplify to total - 2 * knapsack(stones, total // 2)
    return total - 2 * knapsack(stones, total // 2)
