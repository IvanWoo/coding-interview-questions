# https://leetcode.com/problems/binary-watch/
"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:
Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
"""

from typing import List


def bitmask(l, n):
    ans = []
    for i in range(2 ** n, 2 ** (n + 1)):
        b = bin(i)[3:]
        if sum([int(x) for x in b]) == l:
            ans.append(bin(i)[3:])
    return ans


def read_binary_watch(num: int) -> List[str]:
    ans = []

    for i in range(num + 1):
        hrs = bitmask(i, 4)
        mins = bitmask(num - i, 6)
        for hr in hrs:
            hr = int(hr, 2) if hr else 0
            if hr > 11:
                continue
            for m in mins:
                m = int(m, 2) if m else 0
                if m > 59:
                    continue
                ans.append(f"{hr}:{str(m).zfill(2)}")

    return ans


if __name__ == "__main__":
    read_binary_watch(1)
