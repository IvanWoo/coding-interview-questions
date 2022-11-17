# https://leetcode.com/problems/rectangle-area/
"""
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

Example 1:
Rectangle Area
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45

Example 2:
Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16
 
Constraints:
-104 <= ax1 <= ax2 <= 104
-104 <= ay1 <= ay2 <= 104
-104 <= bx1 <= bx2 <= 104
-104 <= by1 <= by2 <= 104
"""


def compute_area(
    ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int
) -> int:
    """
    widely used in machine learning on object detection tasks to calculate the IoU (intersection over union)
    """

    def rect_area(x1, y1, x2, y2):
        width = max((x2 - x1), 0)
        height = max((y2 - y1), 0)
        return width * height

    a_area = rect_area(ax1, ay1, ax2, ay2)
    b_area = rect_area(bx1, by1, bx2, by2)
    overlap_area = rect_area(max(ax1, bx1), max(ay1, by1), min(ax2, bx2), min(ay2, by2))
    return a_area + b_area - overlap_area
