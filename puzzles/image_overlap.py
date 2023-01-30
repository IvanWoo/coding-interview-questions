# https://leetcode.com/problems/image-overlap/
"""
You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.


Example 1:
Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).


Example 2:
Input: img1 = [[1]], img2 = [[1]]
Output: 1

Example 3:
Input: img1 = [[0]], img2 = [[0]]
Output: 0


Constraints:
n == img1.length == img1[i].length
n == img2.length == img2[i].length
1 <= n <= 30
img1[i][j] is either 0 or 1.
img2[i][j] is either 0 or 1.
"""


def largest_overlap(img1: list[list[int]], img2: list[list[int]]) -> int:
    def sum_matrix(img: list[list[int]]):
        ans = 0
        for row in img:
            ans += sum(row)
        return ans

    def translate(img: list[list[int]], vec: list[int]) -> list[list[int]]:
        r, c = len(img), len(img[0])
        ans = [[0 for _ in range(c)] for _ in range(r)]
        dr, dc = vec
        for _r in range(r):
            for _c in range(c):
                nr, nc = _r + dr, _c + dc
                if 0 <= nr < r and 0 <= nc < c:
                    ans[nr][nc] = img[_r][_c]
        return ans

    def overlap(img1: list[list[int]], img2: list[list[int]]) -> int:
        r, c = len(img1), len(img1[0])
        ans = 0
        for _r in range(r):
            for _c in range(c):
                if img1[_r][_c] == img2[_r][_c] == 1:
                    ans += 1
        return ans

    def backtrack(vec: tuple[int]):
        nonlocal seen, ans
        if vec in seen:
            return
        seen.add(vec)
        nxt_img1 = translate(img1, vec)
        if sum_matrix(nxt_img1) <= ans:
            return
        ans = max(ans, overlap(nxt_img1, img2))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nxt_vec = (vec[0] + dr, vec[1] + dc)
            backtrack(nxt_vec)

    max_v = sum_matrix(img2)
    if not max_v:
        return 0
    seen = set()
    ans = 0
    backtrack((0, 0))
    return ans
