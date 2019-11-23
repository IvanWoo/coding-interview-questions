# https://codingbat.com/prob/p238573
"""
Write a function that replaces the words in `raw` with the words in `code_words` such that the first occurrence of each word in `raw` is assigned the first unassigned word in `code_words`.


encoder(["a"], ["1", "2", "3", "4"]) → ["1"]
encoder(["a", "b"], ["1", "2", "3", "4"]) → ["1", "2"]
encoder(["a", "b", "a"], ["1", "2", "3", "4"]) → ["1", "2", "1"]
"""

from typing import List


def encoder(raw: List[str], code_word: List[str]) -> List[str]:
    encode_hashmap = {}
    for w in raw:
        if not encode_hashmap.get(w):
            encode_hashmap[w] = code_word.pop(0)
    return [encode_hashmap[k] for k in raw]
