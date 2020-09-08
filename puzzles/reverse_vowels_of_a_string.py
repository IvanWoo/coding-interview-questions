# https://leetcode.com/problems/reverse-vowels-of-a-string/
"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""


def reverse_vowels(s: str) -> str:
    VOWELS = set("aeiou")
    s_l = list(s)
    lo, hi = 0, len(s_l) - 1
    while lo < hi:
        if s_l[lo].lower() in VOWELS and s_l[hi].lower() in VOWELS:
            s_l[lo], s_l[hi] = s_l[hi], s_l[lo]
            lo += 1
            hi -= 1
        while s_l[lo].lower() not in VOWELS and lo < hi:
            lo += 1
        while s_l[hi].lower() not in VOWELS and lo < hi:
            hi -= 1

    return "".join(s_l)