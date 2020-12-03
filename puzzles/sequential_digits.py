# https://leetcode.com/problems/sequential-digits/
"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
Input: low = 100, high = 300
Output: [123,234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

Constraints:
10 <= low <= high <= 10^9
"""
from typing import List


def sequential_digits(low: int, high: int) -> List[int]:
    def backtrack(val, last_digit):
        if val > high:
            return
        if val >= low:
            res.append(val)
        if last_digit < 9:
            backtrack(val * 10 + (last_digit + 1), last_digit + 1)

    res = []
    for i in range(1, 10):
        backtrack(i, i)
    return sorted(res)


if __name__ == "__main__":
    sequential_digits(100, 300)
