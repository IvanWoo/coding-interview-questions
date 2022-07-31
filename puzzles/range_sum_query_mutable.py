# https://leetcode.com/problems/range-sum-query-mutable/
"""
Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
"""


class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left : right + 1])


# binary indexed tree
class FenwickTree:
    def __init__(self, nums: list[int]):
        n = len(nums)
        self.sum = [0] * (n + 1)

    def _lsb(self, num: int) -> int:
        # least significant bit
        # the lowest 1 and all succeeding 0
        return num & -num

    def update(self, i: int, delta: int) -> None:
        while i < len(self.sum):
            self.sum[i] += delta
            i += self._lsb(i)

    def query(self, i: int) -> int:
        ans = 0
        while i > 0:
            ans += self.sum[i]
            i -= self._lsb(i)
        return ans


class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.tree = self._get_tree(nums)

    def _get_tree(self, nums):
        tree = FenwickTree(nums)
        for i, num in enumerate(nums):
            tree.update(i + 1, num)
        return tree

    def update(self, index: int, val: int) -> None:
        self.tree.update(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(right + 1) - self.tree.query(left)


if __name__ == "__main__":
    nums = [1, 3, 5]
    numArray = NumArray(nums)
    numArray.sumRange(0, 2) == 9
    numArray.update(1, 2)
    numArray.sumRange(0, 2) == 8
