# https://leetcode.com/problems/jump-game-iv/
"""
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

Example 1:
Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

Example 2:
Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.

Example 3:
Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Constraints:
1 <= arr.length <= 5 * 104
-108 <= arr[i] <= 108
"""


from collections import defaultdict, deque


# bfs
def min_jumps(arr: list[int]) -> int:
    def compress(arr):
        ret = [arr[0]]
        cur = arr[0]
        count = 1
        for i in range(1, len(arr)):
            if arr[i] != cur:
                if count > 1:
                    ret.append(cur)
                ret.append(arr[i])
                cur = arr[i]
                count = 1
            else:
                count += 1
        if count > 1:
            ret.append(cur)
        return ret

    arr = compress(arr)
    mappings = defaultdict(list)
    for i, v in enumerate(arr):
        mappings[v].append(i)
    dest = len(arr) - 1
    visited = set()
    q = deque([(0, 0)])
    while q:
        idx, steps = q.popleft()
        if idx in visited or idx < 0 or idx > dest:
            continue
        if idx == dest:
            return steps
        visited.add(idx)
        for nxt_idx in mappings[arr[idx]]:
            q.append((nxt_idx, steps + 1))
        mappings[arr[idx]].clear()
        q.append((idx + 1, steps + 1))
        q.append((idx - 1, steps + 1))
