# https://leetcode.com/problems/walking-robot-simulation/
"""
A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles. 

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.

Example 1:
Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)

Example 2:
Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)

Note:
0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.
"""

from typing import List


class Vector:
    def __init__(self):
        self.x = 0
        self.y = 1
        self.i = 0
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def update(self):
        self.x, self.y = self.dirs[self.i]

    def turn_left(self):
        self.i = (self.i - 1) % 4
        self.update()

    def turn_right(self):
        self.i = (self.i + 1) % 4
        self.update()

    def __repr__(self):
        return f"vector is ({self.x}, {self.y})"


def robot_sim(commands: List[int], obstacles: List[List[int]]) -> int:
    obstacleSet = set(map(tuple, obstacles))
    x, y = 0, 0
    v = Vector()
    ans = 0
    for cmd in commands:
        if cmd == -2:
            v.turn_left()
        elif cmd == -1:
            v.turn_right()
        else:
            while cmd >= 1:
                if (x + v.x, y + v.y) in obstacleSet:
                    break
                else:
                    x += v.x
                    y += v.y
                    cmd -= 1
                    ans = max(ans, x**2 + y**2)
    return ans


if __name__ == "__main__":
    robot_sim([4, -1, 4, -2, 4], [[2, 4]])
