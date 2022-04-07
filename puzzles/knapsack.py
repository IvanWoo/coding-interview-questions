# https://github.com/youngyangyang04/leetcode-master/blob/master/problems/背包理论基础01背包-1.md
"""
有n件物品和一个最多能背重量为w 的背包。
第i件物品的重量是weight[i]，得到的价值是value[i] 。
每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。
"""


def max_value(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n)]

    # initialize
    for j in range(capacity + 1):
        if weights[0] <= j:
            dp[0][j] = values[0]

    for i in range(n):
        for j in range(capacity + 1):
            if j < weights[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])
    return dp[-1][-1]


if __name__ == "__main__":
    max_value([1, 3, 4], [15, 20, 30], 4)
