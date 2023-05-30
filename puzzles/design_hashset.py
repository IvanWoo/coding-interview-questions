# https://leetcode.com/problems/design-hashset/description/
"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)


Constraints:
0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.
"""


class MyHashSet:
    def __init__(self):
        self.db = [0] * (10**6 + 1)

    def add(self, key: int) -> None:
        self.db[key] = 1

    def remove(self, key: int) -> None:
        self.db[key] = 0

    def contains(self, key: int) -> bool:
        return self.db[key] == 1


class MyHashSet:
    def __init__(self):
        self.db = [[] for _ in range(1000)]

    def _get_sub_key(self, key) -> int:
        return key % 1000

    def add(self, key: int) -> None:
        k = self._get_sub_key(key)
        if not self.contains(key):
            self.db[k].append(key)

    def remove(self, key: int) -> None:
        k = self._get_sub_key(key)
        if self.contains(key):
            self.db[k].remove(key)

    def contains(self, key: int) -> bool:
        k = self._get_sub_key(key)
        return key in self.db[k]
