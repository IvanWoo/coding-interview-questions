# https://leetcode.com/problems/palindrome-partitioning/
# backtracking DFS
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

from typing import List


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def decomp_string(
    s: str,
    build_pointer: int,
    decomp_in_progress: List[str],
    valid_decompositions: List[List[str]],
) -> None:
    if build_pointer == len(s):
        valid_decompositions.append(decomp_in_progress)
        return
    for i in range(build_pointer, len(s)):
        snippet = s[build_pointer : i + 1]
        if is_palindrome(snippet):
            decomp_string(
                s, i + 1, decomp_in_progress + [snippet], valid_decompositions
            )


def partition(s: str) -> List[List[str]]:
    """
    time:
        O(n * 2 ^ n)
    space:
        O(n)
    """
    valid_decompositions: List[List[str]] = []
    decomp_in_progress: List[str] = []
    decomp_string(s, 0, decomp_in_progress, valid_decompositions)
    return valid_decompositions


if __name__ == "__main__":
    partition("aab")
