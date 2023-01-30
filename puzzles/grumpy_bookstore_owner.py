# https://leetcode.com/problems/grumpy-bookstore-owner/
"""
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

Example 1:
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

Note:

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1
"""
from typing import List


# TLE: O(n^2)
def max_satisfied(customers: List[int], grumpy: List[int], X: int) -> int:
    n = len(customers)
    _sum = sum([customers[i] for i in range(n) if grumpy[i] == 0])
    res = 0

    for j in range(n - X + 1):
        res = max(res, _sum + sum([customers[i] for i in range(j, j + X) if grumpy[i] == 1]))

    return res


# sliding window: O(n + m) ~= O(n)
def max_satisfied(customers: List[int], grumpy: List[int], X: int) -> int:
    n = len(customers)
    lo, hi = 0, X - 1
    _sum = sum([customers[i] for i in range(n) if grumpy[i] == 0 or lo <= i <= hi])
    res = _sum

    for _ in range(n - X):
        if grumpy[lo] == 1:
            _sum -= customers[lo]
        lo += 1
        hi += 1
        if grumpy[hi] == 1:
            _sum += customers[hi]
        res = max(res, _sum)
    return res


if __name__ == "__main__":
    max_satisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3)
