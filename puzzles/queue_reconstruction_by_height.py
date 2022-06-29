# https://leetcode.com/problems/queue-reconstruction-by-height/
"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.
 
Example
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""


def reconstruct_queue(people: list[list[int]]) -> list[list[int]]:
    people = sorted(people, key=lambda x: (-x[0], x[1]))
    res = []
    for p in people:
        res.insert(p[1], p)
    return res


# O(n^2)
def reconstruct_queue(people: list[list[int]]) -> list[list[int]]:
    n = len(people)
    people = sorted(people)
    ans = [None] * n

    for h, k in people:
        count = 0
        for i in range(n):
            if ans[i] and ans[i][0] < h:
                continue
            if count == k:
                ans[i] = [h, k]
                break
            count += 1
    return ans


if __name__ == "__main__":
    reconstruct_queue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
