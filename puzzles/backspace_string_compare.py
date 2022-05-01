# https://leetcode.com/problems/backspace-string-compare/
"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
"""
from itertools import zip_longest


def backspace_compare(s: str, t: str) -> bool:
    def normalize(s: str) -> str:
        q = []
        for char in s:
            if char == "#":
                if len(q) > 0:
                    q.pop()
            else:
                q.append(char)
        return "".join(q)

    return normalize(s) == normalize(t)


def backspace_compare(s: str, t: str) -> bool:
    # perfect usage of generator
    def gen(s):
        skip = 0
        for char in reversed(s):
            if char == "#":
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield char

    return all(x == y for x, y in zip_longest(gen(s), gen(t)))


if __name__ == "__main__":
    backspace_compare("a##c", "#a#c")
