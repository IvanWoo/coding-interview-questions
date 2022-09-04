# https://leetcode.com/problems/minimum-number-of-refueling-stops/
"""
A car travels from a starting position to a destination which is target miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

Example 1:
Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.

Example 2:
Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).

Example 3:
Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.

Constraints:
1 <= target, startFuel <= 109
0 <= stations.length <= 500
0 <= positioni <= positioni+1 < target
1 <= fueli < 109
"""
from math import inf
from heapq import heappush, heappop

# brute force: TLE
def min_refuel_stops(target: int, start_fuel: int, stations: list[list[int]]) -> int:
    def helper(spot: int, fuel: int, stops: int):
        nonlocal ans
        if spot + fuel >= target:
            ans = min(ans, stops)
            return
        if stops > ans:
            return
        for station, new_fuel in stations:
            if station <= spot:
                continue
            if spot + fuel >= station:
                helper(station, fuel - (station - spot) + new_fuel, stops + 1)

    ans = inf
    helper(0, start_fuel, 0)
    return ans if ans != inf else -1


# dp
def min_refuel_stops(target: int, start_fuel: int, stations: list[list[int]]) -> int:
    dp = [start_fuel] + [0] * len(stations)
    for i, (location, capacity) in enumerate(stations):
        for t in reversed(range(i + 1)):
            if dp[t] >= location:
                dp[t + 1] = max(dp[t + 1], dp[t] + capacity)
    for i, d in enumerate(dp):
        if d >= target:
            return i
    return -1


def min_refuel_stops(target: int, start_fuel: int, stations: list[list[int]]) -> int:
    pq = []
    stations.append(([target, 0]))

    tank = start_fuel
    ans = prev = 0
    for location, capacity in stations:
        tank -= location - prev
        while pq and tank < 0:
            tank += -heappop(pq)
            ans += 1
        if tank < 0:
            return -1
        heappush(pq, -capacity)
        prev = location
    return ans


if __name__ == "__main__":
    min_refuel_stops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]])