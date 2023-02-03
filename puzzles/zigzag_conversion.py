# https://leetcode.com/problems/zigzag-conversion/description/
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


def convert(s: str, num_rows: int) -> str:
    def clamp(x, min_v, max_v):
        return min(max(x, min_v), max_v)

    ans = [[] for _ in range(num_rows)]
    row_idx = 0
    direction = 1
    for char in s:
        if row_idx == num_rows - 1:
            direction = -1
        if row_idx == 0:
            direction = 1
        ans[row_idx].append(char)
        row_idx += direction
        row_idx = clamp(row_idx, 0, num_rows - 1)

    return "".join("".join(row) for row in ans)


def convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s

    ans = [""] * num_rows
    row_idx = 0
    direction = 1
    for char in s:
        if row_idx == num_rows - 1:
            direction = -1
        if row_idx == 0:
            direction = 1
        ans[row_idx] += char
        row_idx += direction

    return "".join(ans)
