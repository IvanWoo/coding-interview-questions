# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:
Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Example 3:
Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
 
Constraints:
1 <= s.length <= 105
s contains only lowercase English letters.
"""

from collections import Counter, defaultdict

# greedy
def min_deletions(s: str) -> int:
    counter = Counter(s)
    count_freq = defaultdict(int)
    max_count = 0
    for _, v in counter.items():
        count_freq[v] += 1
        max_count = max(max_count, v)

    ans = 0
    pointer = max_count
    for count in reversed(range(max_count + 1)):
        pointer = min(pointer, count)
        for _ in range(count_freq[count]):
            if pointer <= count:
                steps = count - pointer
                pointer = max(0, pointer - 1)
                ans += steps
    return ans


if __name__ == "__main__":
    min_deletions("abcabc")
