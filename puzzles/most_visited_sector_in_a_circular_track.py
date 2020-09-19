# https://leetcode.com/problems/most-visited-sector-in-a-circular-track/
"""
Given an integer n and an integer array rounds. We have a circular track which consists of n sectors labeled from 1 to n. A marathon will be held on this track, the marathon consists of m rounds. The ith round starts at sector rounds[i - 1] and ends at sector rounds[i]. For example, round 1 starts at sector rounds[0] and ends at sector rounds[1]

Return an array of the most visited sectors sorted in ascending order.

Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction (See the first example).

Example 1:
Input: n = 4, rounds = [1,3,1,2]
Output: [1,2]
Explanation: The marathon starts at sector 1. The order of the visited sectors is as follows:
1 --> 2 --> 3 (end of round 1) --> 4 --> 1 (end of round 2) --> 2 (end of round 3 and the marathon)
We can see that both sectors 1 and 2 are visited twice and they are the most visited sectors. Sectors 3 and 4 are visited only once.

Example 2:
Input: n = 2, rounds = [2,1,2,1,2,1,2,1,2]
Output: [2]

Example 3:
Input: n = 7, rounds = [1,3,5,7]
Output: [1,2,3,4,5,6,7]

Constraints:

2 <= n <= 100
1 <= m <= 100
rounds.length == m + 1
1 <= rounds[i] <= n
rounds[i] != rounds[i + 1] for 0 <= i < m
"""

from collections import defaultdict
from typing import List


def most_visited(n: int, rounds: List[int]) -> List[int]:
    visits = defaultdict(int)
    start = 0
    while start < len(rounds) - 1:
        p = rounds[start]
        while p != rounds[start + 1]:
            visits[p] += 1
            p %= n
            p += 1
        start += 1
    visits[rounds[start]] += 1
    max_visited = -1
    ans = []
    for k, v in visits.items():
        if v == max_visited:
            ans.append(k)
        elif v > max_visited:
            max_visited = v
            ans = [k]
    return sorted(ans)


def most_visited(n: int, rounds: List[int]) -> List[int]:
    """
    https://leetcode.com/problems/most-visited-sector-in-a-circular-track/discuss/806814/JavaC%2B%2BPython-From-Start-to-End
                    s ----- n
    1 --------------------- n
    1 --------------------- n
    1 ----- e
    """
    start, end = rounds[0], rounds[-1]
    if start <= end:
        return list(range(start, end + 1))
    else:
        return list(range(1, end + 1)) + list(range(start, n + 1))