# https://leetcode.com/problems/unique-substrings-in-wraparound-string/
"""
Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.

Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.

Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
"""

# TLE
def find_substring_in_wrapround_string(p: str) -> int:
    def add(sub_string):
        nonlocal res
        n = len(sub_string)
        temp = set()
        for i in range(n):
            for j in range(i + 1, n + 1):
                temp.add(sub_string[i:j])
        res.update(temp)

    n = len(p)
    if n <= 1:
        return n
    p_int = [ord(x) - ord("a") for x in p]
    res = set()
    i = 0
    while i <= n - 1:
        prev = p_int[i]
        j = i + 1
        while j <= (n - 1) and (prev + 1) % 26 == p_int[j]:
            prev = p_int[j]
            j += 1
        add(p[i:j])
        i = j
    return len(res)


# dp
def find_substring_in_wrapround_string(p: str) -> int:
    p_int = [ord(x) - ord("a") for x in p]
    # res[k] is the maximum length of qualified substring in p that ends with character 'a' + k
    res = [0] * 26
    n = len(p_int)
    for i in p_int:
        res[i] = 1

    l = 1
    for i in range(1, n):
        if (p_int[i - 1] + 1) % 26 == p_int[i]:
            l += 1
        else:
            l = 1
        res[p_int[i]] = max(res[p_int[i]], l)
    return sum(res)


if __name__ == "__main__":
    find_substring_in_wrapround_string("cac")
