# https://leetcode.com/problems/lfu-cache/description/
"""
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.


Example 1:
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3


Constraints:
0 <= capacity <= 104
0 <= key <= 105
0 <= value <= 109
At most 2 * 105 calls will be made to get and put.
"""
from collections import Counter, defaultdict
from math import inf
from time import monotonic_ns

from puzzles.utils import DoublyLinkedList


# TLE
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.count = Counter()
        self.ts = dict()

    def get(self, key: int) -> int:
        val = self.cache.get(key, -1)
        if val != -1:
            self.count[key] += 1
            self.ts[key] = monotonic_ns()
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key not in self.cache and len(self.cache) >= self.capacity:
            invalid_key = self._get_invalid_key()
            del self.cache[invalid_key]
            del self.count[invalid_key]
            del self.ts[invalid_key]
        self.cache[key] = value
        self.count[key] += 1
        self.ts[key] = monotonic_ns()

    def _get_invalid_key(self) -> int:
        kvs = self.count.most_common()
        least_freq = kvs[-1][1]
        candidates = [k for (k, v) in kvs if v == least_freq]
        invalid_key = None
        min_ts = inf
        for c in candidates:
            if self.ts[c] < min_ts:
                min_ts = self.ts[c]
                invalid_key = c
        return invalid_key


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfu_count = 0
        self.cache = dict()
        # map{key -> count}
        self.count = defaultdict(int)
        # map{count -> [key]}
        self.freq = defaultdict(DoublyLinkedList)

    def counter(self, key):
        cnt = self.count[key]
        self.count[key] += 1
        self.freq[cnt].pop(key)
        self.freq[cnt + 1].push_right(key)

        if cnt == self.lfu_count and self.freq[cnt].length() == 0:
            self.lfu_count += 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.counter(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key not in self.cache and len(self.cache) == self.capacity:
            res = self.freq[self.lfu_count].pop_left()
            del self.cache[res]
            del self.count[res]

        self.cache[key] = value
        self.counter(key)
        self.lfu_count = min(self.lfu_count, self.count[key])
