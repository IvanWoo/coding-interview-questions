# https://leetcode.com/problems/accounts-merge/
"""
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:

Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""
from typing import List
from collections import defaultdict


def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
    parent = dict()
    size = dict()

    def add(x):
        parent.setdefault(x, x)
        size.setdefault(x, 1)

    def find(x):
        while parent[x] != x:
            # path compression
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        add(x)
        add(y)
        px, py = find(x), find(y)
        if px == py:
            return

        if size[py] > size[px]:
            parent[px] = py
            size[py] += size[px]
        else:
            parent[py] = px
            size[px] += size[py]

    em_to_name = {}
    for account in accounts:
        name, emails = account[0], account[1:]
        for email in emails:
            em_to_name[email] = name
            # core skill: just connect the first email with all of the others
            union(emails[0], email)

    res = defaultdict(list)
    for email in em_to_name.keys():
        res[find(email)].append(email)

    return [[em_to_name[k]] + sorted(v) for k, v in res.items()]


if __name__ == "__main__":
    accounts_merge(
        [
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"],
        ]
    )
