# https://leetcode.com/problems/kth-missing-positive-number/
"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.


Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.


Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
"""


def find_kth_positive(arr: list[int], k: int) -> int:
    arr_set = set(arr)
    curr = 1
    while k > 0:
        if curr not in arr_set:
            k -= 1
        curr += 1
    return curr - 1


def find_kth_positive(arr: list[int], k: int) -> int:
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] - mid - 1 < k:
            lo = mid + 1
        else:
            hi = mid
    return lo + k
