# https://leetcode.com/problems/search-suggestions-system/
"""
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:
Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:
Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
 
Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TrieNode:
    children: dict[str, TrieNode] = field(default_factory=dict)
    value: list[str] = field(default_factory=list)


class ProductDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, product: str) -> None:
        node = self.root
        for char in product:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.value.append(product)
        return

    def search(self, word: str) -> list[str]:
        node = self.root
        for char in word:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.value[:3]


def suggested_products(products: list[str], searchWord: str) -> list[list[str]]:
    products.sort()
    pd = ProductDictionary()
    for product in products:
        pd.insert(product)

    ans = []
    n = len(searchWord)
    for i in range(1, n + 1):
        ans.append(pd.search(searchWord[:i]))
    return ans


from bisect import bisect_left


def suggested_products(products: list[str], searchWord: str) -> list[list[str]]:
    products.sort()
    ans, prefix, i = [], "", 0
    for char in searchWord:
        prefix += char
        i = bisect_left(products, prefix, i)
        ans.append([w for w in products[i : i + 3] if w.startswith(prefix)])
    return ans


if __name__ == "__main__":
    suggested_products(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse")
