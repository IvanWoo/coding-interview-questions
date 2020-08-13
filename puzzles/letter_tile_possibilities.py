# https://leetcode.com/problems/letter-tile-possibilities/
"""
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: "AAABBC"
Output: 188

Note:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""


def num_tile_possibilities(tiles: str) -> int:
    poss = set()

    def backtrack(tiles, seq):
        if seq:
            poss.add(seq)
        for i, char in enumerate(tiles):
            backtrack(tiles[:i] + tiles[i + 1 :], seq + char)

    backtrack(tiles, "")
    return len(poss)

