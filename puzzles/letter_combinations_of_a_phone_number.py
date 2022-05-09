# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""


def letter_combinations(digits: str) -> list[str]:
    int_to_letters = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }

    res = []

    def helper(digits: str, path: str):
        nonlocal res
        if not digits:
            if path:
                res.append(path)
            return
        d, nxt_digits = digits[0], digits[1:]
        for nxt in int_to_letters[int(d)]:
            helper(nxt_digits, path + nxt)

    helper(digits, "")

    return res
