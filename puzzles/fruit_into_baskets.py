# https://leetcode.com/problems/fruit-into-baskets/
"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].


Constraints:
1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
"""
from collections import defaultdict


# brute force
def total_fruit(fruits: list[int]) -> int:
    def backtrack(types, count, idx):
        nonlocal ans
        ans = max(ans, count)
        if idx == n:
            return
        match len(types):
            case 0:
                backtrack(types, count, idx + 1)
                backtrack([fruits[idx]], count + 1, idx + 1)
            case 1:
                if fruits[idx] in types:
                    backtrack(types, count + 1, idx + 1)
                else:
                    backtrack(types + [fruits[idx]], count + 1, idx + 1)
            case 2:
                if fruits[idx] in types:
                    backtrack(types, count + 1, idx + 1)

    ans = 0
    n = len(fruits)
    backtrack([], 0, 0)
    return ans


# sliding window
def total_fruit(fruits: list[int]) -> int:
    basket = defaultdict(int)
    j = 0
    ans = 0
    for i, fruit in enumerate(fruits):
        basket[fruit] += 1
        while len(basket) > 2:
            basket[fruits[j]] -= 1
            if basket[fruits[j]] == 0:
                del basket[fruits[j]]
            j += 1
        ans = max(ans, i - j + 1)
    return ans


total_fruit([1, 2, 3, 2, 2])
