# https://leetcode.com/problems/rotate-image/
"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""


def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for layer in range(n // 2):
        # print(f"{layer=}")
        for step in range(n - layer * 2 - 1):
            # print(f"{step=}")
            e0, e1, e2, e3 = (
                (layer, layer + step),
                (layer + step, n - layer - 1),
                (n - layer - 1, n - layer - 1 - step),
                (n - layer - 1 - step, layer),
            )
            # print(e0, e1, e2, e3)
            (
                matrix[e0[0]][e0[1]],
                matrix[e1[0]][e1[1]],
                matrix[e2[0]][e2[1]],
                matrix[e3[0]][e3[1]],
            ) = (
                matrix[e3[0]][e3[1]],
                matrix[e0[0]][e0[1]],
                matrix[e1[0]][e1[1]],
                matrix[e2[0]][e2[1]],
            )


if __name__ == "__main__":
    rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
