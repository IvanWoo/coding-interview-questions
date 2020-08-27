# https://leetcode.com/problems/reverse-only-letters/
"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain '\' or "
"""


def reverse_only_letters(S: str) -> str:
    n = len(S)
    ans = [""] * n
    for i, char in enumerate(S):
        if not char.isalpha():
            ans[i] = char

    i, j = 0, n - 1
    while i < n and j >= 0:
        if S[i].isalpha():
            while ans[j]:
                j -= 1
            ans[j] = S[i]
        i += 1

    return "".join(ans)


def reverse_only_letters(S: str) -> str:
    S = list(S)
    i, j = 0, len(S) - 1
    while i < j:
        if not S[i].isalpha():
            i += 1
        elif not S[j].isalpha():
            j -= 1
        else:
            S[i], S[j] = S[j], S[i]
            i += 1
            j -= 1
    return "".join(S)
