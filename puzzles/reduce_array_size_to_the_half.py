# https://leetcode.com/problems/reduce-array-size-to-the-half/
"""
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

Example 1:
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

Example 2:
Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.


Constraints:
2 <= arr.length <= 105
arr.length is even.
1 <= arr[i] <= 105
"""
from collections import Counter, defaultdict
from heapq import heappop, heappush


def min_set_size(arr: list[int]) -> int:
    n = len(arr)
    c = Counter(arr)
    ans = 0
    total = 0
    for _, v in c.most_common():
        if total >= n // 2:
            break
        total += v
        ans += 1
    return ans


# priority queue
def min_set_size(arr: list[int]) -> int:
    n = len(arr)
    pq = []
    counter = defaultdict(int)
    for val in arr:
        counter[val] += 1
    for _, v in counter.items():
        heappush(pq, -v)

    ans = 0
    total = 0
    while pq:
        if total >= n // 2:
            break
        total -= heappop(pq)
        ans += 1
    return ans


def min_set_size(arr: list[int]) -> int:
    n = len(arr)
    counter = defaultdict(int)
    for val in arr:
        counter[val] += 1

    ans = 0
    total = 0
    # copy the Counter.most_common() implementation
    # https://github.com/python/cpython/blob/586fc02be5b3e103bfddd49654034a898a8d6dfc/Lib/collections/__init__.py#L616-L618
    for _, v in sorted(counter.items(), key=lambda x: x[1], reverse=True):
        if total >= n // 2:
            break
        total += v
        ans += 1
    return ans
