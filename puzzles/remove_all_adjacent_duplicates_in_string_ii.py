# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"


Constraints:
1 <= s.length <= 105
2 <= k <= 104
s only contains lower case English letters.
"""
from collections import deque


def remove_duplicates(s: str, k: int) -> str:
    def concat(stack: list[str]) -> str:
        return "".join(char * count for (char, count) in stack)

    while True:
        stack = []
        curr = None
        removed = False
        for char in s:
            if curr is None:
                curr = char
                count = 1
                continue
            if char == curr:
                count += 1
            else:
                stack.append((curr, count))
                curr = char
                count = 1
            if count == k:
                count = 0
                curr = None
                removed = True
        if curr:
            stack.append((curr, count))
        if not removed:
            break

        s = concat(stack)
    return concat(stack)


def remove_duplicates(s: str, k: int) -> str:
    stack = deque()
    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([char, 1])
    return "".join(char * count for (char, count) in stack)


if __name__ == "__main__":
    remove_duplicates("pbbcggttciiippooaais", 2)
