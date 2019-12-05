# https://leetcode.com/problems/hamming-distance/
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""


def hamming_distance(x: int, y: int) -> int:
    res = 0
    bs = sorted([bin(x)[2:][::-1], bin(y)[2:][::-1]], key=len)
    for k, v in enumerate(bs[0]):
        if bs[1][k] != v:
            res += 1
    return res + len([i for i in bs[1][k + 1 :] if i == "1"])


# bitwise xor is more expensive than above
def hamming_distance(x: int, y: int) -> int:
    return len([i for i in bin(x ^ y) if i == "1"])
