# https://leetcode.com/problems/construct-string-from-binary-tree/
"""
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"

Example 2:
Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-1000 <= Node.val <= 1000
"""
from typing import Optional

from puzzles.utils import TreeNode, make_tree


def tree2str(root: Optional[TreeNode]) -> str:
    def traverse(node: TreeNode) -> Optional[str]:
        if not node:
            return
        left = traverse(node.left)
        right = traverse(node.right)

        child = ""
        match (left, right):
            case (None, None):
                child = ""
            case (None, _):
                child = f"()({right})"
            case (_, None):
                child = f"({left})"
            case _:
                child = f"({left})({right})"

        return f"{node.val}{child}"

    return traverse(root)


if __name__ == "__main__":
    tree2str(make_tree([1, 2, 3, 4]))
