# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6

Constraints:
1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 109
1 <= profit[i] <= 104
"""
from bisect import bisect_left
from functools import cache


def job_scheduling(
    start_time: list[int], end_time: list[int], profit: list[int]
) -> int:
    @cache
    def dp(i):
        if i == n:
            return 0
        j = i + 1
        while j < n and jobs[i][1] > jobs[j][0]:
            j += 1
        # pick or skip job i
        return max(jobs[i][2] + dp(j), dp(i + 1))

    n = len(start_time)
    jobs = sorted(zip(start_time, end_time, profit))
    return dp(0)


def job_scheduling(
    start_time: list[int], end_time: list[int], profit: list[int]
) -> int:
    @cache
    def dp(i):
        if i == n:
            return 0
        j = bisect_left(start_time, jobs[i][1])
        # pick or skip job i
        return max(jobs[i][2] + dp(j), dp(i + 1))

    n = len(start_time)
    jobs = sorted(zip(start_time, end_time, profit))
    start_time.sort()
    return dp(0)
