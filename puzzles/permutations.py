import itertools
from collections import deque


class Permutatons:
    def __init__(self):
        self.res = deque()

    def permutations(self, nums):
        track = deque()
        self.backtrack(nums, track)
        return list(self.res)

    def backtrack(self, nums, track):
        if len(track) == len(nums):
            self.res.append(tuple(track))
            return

        for i in nums:
            if i in track:
                continue
            track.append(i)
            self.backtrack(nums, track)
            track.pop()


if __name__ == "__main__":
    a_list = [1, 2, 3, 5, 6]
    p = Permutatons()
    print(f"{p.permutations(a_list) == list(itertools.permutations(a_list)) = }")
