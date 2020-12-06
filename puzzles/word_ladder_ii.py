# https://leetcode.com/problems/word-ladder-ii/
"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
import string
from typing import List
from collections import defaultdict

# TLE
def find_ladders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    if endWord not in wordList:
        return []
    word_set = set(wordList + [beginWord])
    graph = defaultdict(set)
    for w in word_set:
        for i in range(len(w)):
            for c in string.ascii_lowercase:
                if c == w[i]:
                    continue
                new_w = w[:i] + c + w[i + 1 :]
                if new_w in word_set:
                    graph[w].add(new_w)

    shortest = float("inf")
    res = []

    def helper(w, path):
        nonlocal res, shortest
        if len(path) > shortest:
            return
        if w == endWord:
            if len(path) == shortest:
                res.append(path[:])
            elif len(path) < shortest:
                res = [path[:]]
                shortest = len(path)
            return

        for neighbor in graph[w]:
            if neighbor in path:
                continue
            path.append(neighbor)
            helper(neighbor, path)
            path.pop()

    helper(beginWord, [beginWord])
    return res


if __name__ == "__main__":
    find_ladders(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"],
    ) == [
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"],
    ]
