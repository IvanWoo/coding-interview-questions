# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
"""
Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

SummaryRanges() Initializes the object with an empty stream.
void addNum(int value) Adds the integer value to the stream.
int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
 

Example 1:
Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
 

Constraints:
0 <= value <= 104
At most 3 * 104 calls will be made to addNum and getIntervals.
 

Follow up: What if there are lots of merges and the number of disjoint intervals is small compared to the size of the data stream?
"""
from bisect import insort
from sortedcontainers import SortedSet


class SummaryRanges:
    def __init__(self):
        self.data = []
        self.vals = set()

    def addNum(self, value: int) -> None:
        if value in self.vals:
            return
        insort(self.data, value)
        self.vals.add(value)

    def getIntervals(self) -> list[list[int]]:
        intervals = []
        cur = self.data[0]
        count = 1
        for v in self.data[1:]:
            if v == cur + count:
                count += 1
            else:
                intervals.append([cur, cur + count - 1])
                cur = v
                count = 1
        intervals.append([cur, cur + count - 1])

        return intervals


class SummaryRanges:
    def __init__(self):
        self.data = SortedSet()

    def addNum(self, value: int) -> None:
        self.data.add(value)

    def getIntervals(self) -> list[list[int]]:
        intervals = []
        cur = self.data[0]
        count = 1
        for v in self.data[1:]:
            if v == cur + count:
                count += 1
            else:
                intervals.append([cur, cur + count - 1])
                cur = v
                count = 1
        intervals.append([cur, cur + count - 1])

        return intervals


class SummaryRanges:
    def __init__(self):
        self.data = set()

    def addNum(self, value: int) -> None:
        self.data.add(value)

    def getIntervals(self) -> list[list[int]]:
        intervals = []
        visited = set()
        for v in self.data:
            if v in visited:
                continue
            visited.add(v)
            left = v
            while left - 1 in self.data:
                left -= 1
                visited.add(left)

            right = v
            while right + 1 in self.data:
                right += 1
                visited.add(right)

            intervals.append([left, right])

        return sorted(intervals)


if __name__ == "__main__":
    sr = SummaryRanges()
    sr.addNum(1)
    sr.addNum(3)
    sr.getIntervals()
