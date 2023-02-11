# https://leetcode.com/problems/naming-a-company/
"""

You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

Choose 2 distinct names from ideas, call them ideaA and ideaB.
Swap the first letters of ideaA and ideaB with each other.
If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.

Example 1:
Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6
Explanation: The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.

The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.

Example 2:
Input: ideas = ["lack","back"]
Output: 0
Explanation: There are no valid selections. Therefore, 0 is returned.


Constraints:
2 <= ideas.length <= 5 * 104
1 <= ideas[i].length <= 10
ideas[i] consists of lowercase English letters.
All the strings in ideas are unique."""
from collections import defaultdict


# brute force: TLE
def distinct_names(ideas: list[str]) -> int:
    def is_valid(i1: str, i2: str) -> bool:
        s1, s2 = i2[0] + i1[1:], i1[0] + i2[1:]
        return s1 not in ideas_set and s2 not in ideas_set

    ideas_set = set(ideas)
    n = len(ideas)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if is_valid(ideas[i], ideas[j]):
                ans += 1
    return ans * 2


def distinct_names(ideas: list[str]) -> int:
    initial_map = defaultdict(set)
    for idea in ideas:
        head, tail = idea[0], idea[1:]
        initial_map[head].add(tail)
    ans = 0
    keys = initial_map.keys()
    for x in keys:
        for y in keys:
            x_set, y_set = initial_map[x], initial_map[y]
            intersection = x_set.intersection(y_set)
            ans += len(x_set - intersection) * len(y_set - intersection)
    return ans


def distinct_names(ideas: list[str]) -> int:
    initial_map = defaultdict(set)
    for idea in ideas:
        head, tail = idea[0], idea[1:]
        initial_map[head].add(tail)
    ans = 0
    for x, x_set in initial_map.items():
        for y, y_set in initial_map.items():
            if x >= y:
                continue
            intersection = len(x_set.intersection(y_set))
            ans += (len(x_set) - intersection) * (len(y_set) - intersection)
    return ans * 2