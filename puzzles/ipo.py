# https://leetcode.com/problems/ipo/
"""
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given several projects. For each project i, it has a pure profit Pi and a minimum capital of Ci is needed to start the corresponding project. Initially, you have W capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

To sum up, pick a list of at most k distinct projects from given projects to maximize your final capital, and output your final maximized capital.

Example 1:

Input: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].

Output: 4

Explanation: Since your initial capital is 0, you can only start the project indexed 0.
             After finishing it you will obtain profit 1 and your capital becomes 1.
             With capital 1, you can either start the project indexed 1 or the project indexed 2.
             Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
             Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Note:

You may assume all numbers in the input are non-negative integers.
The length of Profits array and Capital array will not exceed 50,000.
The answer is guaranteed to fit in a 32-bit signed integer.
"""
import heapq


def find_maximized_capital(
    k: int, w: int, profits: list[int], capital: list[int]
) -> int:
    n = len(profits)
    cp = sorted(zip(capital, profits))
    pq = []
    i = 0

    while k > 0:
        while i < n and cp[i][0] <= w:
            heapq.heappush(pq, -cp[i][1])
            i += 1
        if not pq:
            break
        w -= heapq.heappop(pq)
        k -= 1
    return w


if __name__ == "__main__":
    find_maximized_capital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1])
