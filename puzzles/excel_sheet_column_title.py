# https://leetcode.com/problems/excel-sheet-column-title/
"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...

Example 1:
Input: 1
Output: "A"

Example 2:
Input: 28
Output: "AB"

Example 3:
Input: 701
Output: "ZY"
"""


def convert_to_title(n: int) -> str:
    ans = []
    while n != 0:
        q, r = divmod(n - 1, 26)
        n = q
        ans.append(r)
    return "".join([chr(ord("A") + i) for i in reversed(ans)])
