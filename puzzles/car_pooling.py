# https://leetcode.com/problems/car-pooling/
"""
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 
 

Example 1:
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Example 3:
Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true

Example 4:
Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
 

Constraints:

trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000
"""
from typing import List

# naive scan
def car_pooling(trips: List[List[int]], capacity: int) -> bool:
    start = min([x[1] for x in trips])
    end = max([x[2] for x in trips])

    for i in range(start, end + 1):
        if sum([x[0] for x in trips if x[1] <= i < x[2]]) > capacity:
            return False
    return True


def car_pooling(trips: List[List[int]], capacity: int) -> bool:
    timestamps = []
    for trip in trips:
        timestamps.append((trip[1], trip[0]))
        timestamps.append((trip[2], -trip[0]))

    timestamps.sort()
    used_capacity = 0
    for _, change in timestamps:
        used_capacity += change
        if used_capacity > capacity:
            return False
    return True