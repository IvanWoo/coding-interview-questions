# https://leetcode.com/problems/binary-trees-with-factors/
"""
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

Example 1:
Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Example 2:
Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

Constraints:
1 <= arr.length <= 1000
2 <= arr[i] <= 109
All the values of arr are unique.
"""


def num_factored_binary_trees(arr: list[int]) -> int:
    arr = sorted(arr)
    n = len(arr)
    index = {val: i for i, val in enumerate(arr)}

    dp = [1] * n

    for i, x in enumerate(arr):
        for j in range(i):
            other, left = divmod(x, arr[j])
            if left:
                continue
            if other in index:
                dp[i] += dp[j] * dp[index[other]]
    MOD = 10**9 + 7
    return sum(dp) % MOD


if __name__ == "__main__":
    num_factored_binary_trees([18, 3, 6, 2])
