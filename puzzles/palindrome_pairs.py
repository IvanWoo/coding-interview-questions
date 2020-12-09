# https://leetcode.com/problems/palindrome-pairs/
"""
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example 1:
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:
Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:
Input: words = ["a",""]
Output: [[0,1],[1,0]]
 
Constraints:
1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.
"""
from typing import List

# TLE
def palindrome_pairs(words: List[str]) -> List[List[int]]:
    def is_palindrome(s):
        return s == s[::-1]

    n = len(words)
    res = []
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            if is_palindrome(words[i] + words[j]):
                res.append([i, j])
    return res


def palindrome_pairs(words: List[str]) -> List[List[int]]:
    def partial_palindrome(word, left):
        # test word[left:] is parlindrom or not
        right = len(word) - 1
        while left <= right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True

    class TrieNode:
        def __init__(self):
            self.word_index = -1
            self.value = None
            self.list = []
            self.children = dict()

    class Trie:
        def __init__(self):
            self.root = TrieNode()

        def insert(self, word, index):
            node = self.root
            for j, char in enumerate(word):
                if partial_palindrome(word, j):
                    node.list.append(index)
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word_index = index
            node.value = word

    def get_candidates(trie, word, i):
        candidates = []
        node = trie.root
        reversed_word = word[::-1]
        for j, char in enumerate(reversed_word):
            # reversed_word is longer than canadidate
            if node.word_index != -1 and partial_palindrome(reversed_word, j):
                candidates.append(node.word_index)
            if char not in node.children:
                break
            node = node.children[char]
        else:
            # canadidate == reversed_word[::-1]
            if node.word_index not in [-1, i]:
                candidates.append(node.word_index)
            # canadidate = abc|sos, reversed_word = cba
            for k in node.list:
                candidates.append(k)
        return candidates

    trie = Trie()
    for index, word in enumerate(words):
        trie.insert(word, index)

    res = []
    for i, word in enumerate(words):
        candidates = get_candidates(trie, word, i)
        res.extend([[c, i] for c in candidates])
    return res


if __name__ == "__main__":
    palindrome_pairs(["a", ""])
    palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
