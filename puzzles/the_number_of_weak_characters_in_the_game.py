# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
"""
You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.

Example 1:
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.

Example 2:
Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.

Example 3:
Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.


Constraints:
2 <= properties.length <= 105
properties[i].length == 2
1 <= attacki, defensei <= 105
"""
from math import inf


# brute force: O(n^2)
def number_of_weak_characters(properties: list[list[int]]) -> int:
    def is_weak(i, j):
        ai, di = properties[i]
        aj, dj = properties[j]
        if ai < aj and di < dj:
            return i
        if ai > aj and di > dj:
            return j
        return

    n = len(properties)
    ans = set()
    for i in range(n):
        for j in range(i):
            idx = is_weak(i, j)
            if idx is not None:
                ans.add(idx)
    return len(ans)


def number_of_weak_characters(properties: list[list[int]]) -> int:
    sorted_p = sorted(properties, key=lambda x: (x[0], -x[1]))
    stack = []
    ans = 0
    for _, d in sorted_p:
        while stack and stack[-1] < d:
            stack.pop()
            ans += 1
        stack.append(d)
    return ans


def number_of_weak_characters(properties: list[list[int]]) -> int:
    sorted_p = sorted(properties, key=lambda x: (x[0], -x[1]))
    max_d = -inf
    ans = 0
    for _, d in reversed(sorted_p):
        if d < max_d:
            ans += 1
        max_d = max(d, max_d)
    return ans


if __name__ == "__main__":
    number_of_weak_characters([[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]])
