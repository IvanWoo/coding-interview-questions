# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
"""
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.


Example 1:
Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7

Example 2:
Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.

Example 3:
Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.


Constraints:
1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10
"""
from functools import cache
from math import inf


def min_difficulty(job_difficulty: list[int], d: int) -> int:
    @cache
    def helper(i: int, d: int) -> int:
        # i: previous cut index
        # d: left days
        if d == 1:
            return max(job_difficulty[i:])
        res, max_v = inf, 0
        for j in range(i, n - d + 1):
            max_v = max(max_v, job_difficulty[j])
            res = min(res, max_v + helper(j + 1, d - 1))
        return res

    n = len(job_difficulty)
    if n < d:
        return -1

    return helper(0, d)


if __name__ == "__main__":
    min_difficulty([6, 5, 4, 3, 2, 1], 2)
