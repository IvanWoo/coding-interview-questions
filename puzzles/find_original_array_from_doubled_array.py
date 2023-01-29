# https://leetcode.com/problems/find-original-array-from-doubled-array/
"""
An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.


Example 1:
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:
Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:
Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.
 

Constraints:
1 <= changed.length <= 105
0 <= changed[i] <= 105
"""
from collections import Counter, defaultdict, deque


def find_original_array(changed: list[int]) -> list[int]:
    n = len(changed)
    if n % 2 == 1:
        return []

    changed.sort()
    counter = defaultdict(deque)
    for i, v in enumerate(changed):
        counter[v].append(i)
    visited = set()
    ans = []
    for i, v in enumerate(changed):
        if i in visited:
            continue
        visited.add(counter[v].popleft())
        ans.append(v)
        if not counter[v * 2]:
            return []
        visited.add(counter[v * 2].popleft())
    return ans


def find_original_array(changed: list[int]) -> list[int]:
    n = len(changed)
    if n % 2 == 1:
        return []

    c = Counter(changed)
    for x in sorted(c):
        if c[x] > c[x * 2]:
            return []
        c[x * 2] -= c[x] if x else c[x] // 2
    return list(c.elements())


if __name__ == "__main__":
    find_original_array([1, 3, 4, 2, 6, 8])
