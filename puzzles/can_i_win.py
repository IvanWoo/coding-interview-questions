# https://leetcode.com/problems/can-i-win/
"""
In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise return false. Assume both players play optimally.

Example 1:
Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.

Example 2:
Input: maxChoosableInteger = 10, desiredTotal = 0
Output: true

Example 3:
Input: maxChoosableInteger = 10, desiredTotal = 1
Output: true

Constraints:
1 <= maxChoosableInteger <= 20
0 <= desiredTotal <= 300
"""


def can_i_win(maxChoosableInteger: int, desiredTotal: int) -> bool:
    def helper(choices, target):
        nonlocal visited
        if choices[-1] >= target:
            return True
        visited_key = tuple(choices)
        if visited_key in visited:
            return visited[visited_key]

        # next player's turn
        n = len(choices)
        for i in range(n):
            if not helper(choices[:i] + choices[i + 1 :], target - choices[i]):
                visited[visited_key] = True
                return True

        visited[visited_key] = False
        return False

    if desiredTotal <= maxChoosableInteger:
        return True
    total = sum(range(maxChoosableInteger + 1))
    if total < desiredTotal:
        return False
    if total == desiredTotal:
        return maxChoosableInteger % 2 == 1
    visited = dict()
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)


if __name__ == "__main__":
    can_i_win(10, 40)