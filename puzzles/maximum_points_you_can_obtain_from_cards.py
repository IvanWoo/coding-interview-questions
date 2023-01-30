# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
"""
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.


Constraints:
1 <= cardPoints.length <= 105
1 <= cardPoints[i] <= 104
1 <= k <= cardPoints.length
"""
from functools import cache
from math import inf


# brute force: MLE
def max_score(card_points: list[int], k: int) -> int:
    @cache
    def helper(start: int, end: int, left: int, total_points: int) -> int:
        if left == 0:
            return total_points

        return max(
            helper(start + 1, end, left - 1, total_points + card_points[start]),
            helper(start, end - 1, left - 1, total_points + card_points[end]),
        )

    n = len(card_points)
    start, end = 0, n - 1
    return helper(start, end, k, 0)


# prefix sum: O(n)
def max_score(card_points: list[int], k: int) -> int:
    def prefix_sum(l: list[int]) -> list[int]:
        n = len(l)
        res = l[:]
        for i in range(1, n):
            res[i] += res[i - 1]
        return [0] + res

    left = prefix_sum(card_points)
    right = prefix_sum(card_points[::-1])
    res = -inf
    for i in range(k + 1):
        res = max(res, left[i] + right[k - i])
    return res


# sliding window
def max_score(card_points: list[int], k: int) -> int:
    total = sum(card_points)
    n = len(card_points)
    if n == k:
        return total
    left, right = 0, n - k
    win_sum = sum(card_points[left:right])
    ans = 0
    while right <= n:
        ans = max(ans, total - win_sum)
        win_sum -= card_points[left]
        if right < n:
            win_sum += card_points[right]
        left += 1
        right += 1
    return ans
