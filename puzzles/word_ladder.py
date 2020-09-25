# https://leetcode.com/problems/word-ladder/
"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""


from typing import List
from collections import defaultdict, deque


def ladder_length(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0
    l = len(beginWord)
    word_dict = defaultdict(list)
    for word in wordList:
        for i in range(l):
            word_dict[word[:i] + "*" + word[i + 1 :]].append(word)

    # bfs
    q = deque([(beginWord, 1)])
    visited = set()
    while q:
        cur_word, level = q.popleft()
        for i in range(l):
            intermediate_word = cur_word[:i] + "*" + cur_word[i + 1 :]

            for word in word_dict[intermediate_word]:
                if word == endWord:
                    return level + 1

                if word not in visited:
                    visited.add(word)
                    q.append((word, level + 1))
            # tried every mutations for intermediate_word and remove it from potential paths
            word_dict[intermediate_word] = []

    return 0
