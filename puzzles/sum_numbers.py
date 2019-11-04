# https://codingbat.com/prob/p121193
"""
Given a string, return the sum of the numbers appearing in the string, ignoring all other characters. A number is a series of 1 or more digit chars in a row. (Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)


sumNumbers("abc123xyz") → 123
sumNumbers("aa11b33") → 44
sumNumbers("7 11") → 18
"""


def sum_numbers(s: str) -> int:
    # replace non-digit with blank space
    new_s = "".join([x if x.isdigit() else " " for x in s])
    return sum([int(x) for x in new_s.strip().split(" ")])
