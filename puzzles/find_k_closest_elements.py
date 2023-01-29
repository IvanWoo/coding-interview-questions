# https://leetcode.com/problems/find-k-closest-elements/
"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:
1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""
import heapq


# O(NlogN)
def find_closest_elements(arr: list[int], k: int, x: int) -> list[int]:
    pq = []
    for i, a in enumerate(arr):
        if len(pq) < k:
            heapq.heappush(pq, (-abs(a - x), -a, i))
        else:
            cur = heapq.heappop(pq)
            if -abs(a - x) > cur[0] or (-abs(a - x) == cur[0] and -a > cur[1]):
                heapq.heappush(pq, (-abs(a - x), -a, i))
            else:
                heapq.heappush(pq, cur)

    pq = sorted(pq, key=lambda x: x[2])
    return [-x[1] for x in pq]


def find_closest_elements(arr: list[int], k: int, x: int) -> list[int]:
    lo, hi = 0, len(arr) - k
    while lo < hi:
        mid = (lo + hi) >> 1
        if x > (arr[mid + k] + arr[mid]) / 2:
            lo = mid + 1
        else:
            hi = mid
    return arr[lo : lo + k]


if __name__ == "__main__":
    find_closest_elements([1, 1, 1, 10, 10, 10], 1, 9)
