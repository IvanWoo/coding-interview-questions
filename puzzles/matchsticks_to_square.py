# https://leetcode.com/problems/matchsticks-to-square/
"""
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.

Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.
"""


# dfs: O(4^n)
def makesquare(nums: list[int]) -> bool:
    if not nums:
        return False
    total = sum(nums)
    target_len = total // 4
    if total / 4 != target_len:
        return False

    n = len(nums)
    q = [(0, [0, 0, 0, 0])]
    while q:
        index, lens = q.pop()
        if index == n:
            return True
        for k in range(4):
            if lens[k] + nums[index] <= target_len:
                new_lens = list(lens)
                new_lens[k] += nums[index]
                q.append((index + 1, new_lens))
    return False


# dfs: O(4^n)
def makesquare(nums: list[int]) -> bool:
    if not nums:
        return False
    total = sum(nums)
    target_len = total // 4
    if total / 4 != target_len:
        return False

    n = len(nums)

    def helper(i, lens):
        if i == n:
            return True
        visited = set()
        for j in range(4):
            if (
                lens[j] == target_len
                or (lens[j] + nums[i] > target_len)
                or lens[j] in visited
            ):
                continue
            lens[j] += nums[i]
            if helper(i + 1, lens):
                return True
            lens[j] -= nums[i]
            visited.add(lens[j])
        return False

    lens = [0] * 4
    return helper(0, lens)


def makesquare(nums: list[int]) -> bool:
    def dfs(nums, pos, target, temp_sum, group_id, visited):
        if group_id == 4:
            return True
        if temp_sum == target:
            return dfs(nums, 0, target, 0, group_id + 1, visited)
        if temp_sum > target:
            return False
        for i in range(pos, len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue
            visited[i] = True
            if dfs(nums, i + 1, target, temp_sum + nums[i], group_id, visited):
                return True
            visited[i] = False
        return False

    if not nums:
        return False
    total = sum(nums)
    target_len = total // 4
    if total / 4 != target_len:
        return False
    n = len(nums)
    visited = [False] * n
    nums.sort()
    return dfs(nums, 0, target_len, 0, 1, visited)


def makesquare(matchsticks: list[int]) -> bool:
    def backtrack(visited, acc):
        nonlocal can, n, target
        if can:
            return
        if acc > target:
            return
        if acc == target:
            acc = 0
        if len(visited) == n:
            can = True
            return
        for i in range(n):
            if i in visited:
                continue
            val = matchsticks[i]
            visited.add(i)
            backtrack(visited, acc + val)
            visited.remove(i)

    total = sum(matchsticks)
    target = total // 4
    if total / 4 != target:
        return False
    n = len(matchsticks)
    can = False

    backtrack(set(), 0)
    return can
