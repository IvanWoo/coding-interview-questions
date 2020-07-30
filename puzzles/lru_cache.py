# https://github.com/labuladong/fucking-algorithm/blob/master/高频面试系列/LRU算法.md
# https://leetcode.com/problems/lru-cache/

"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # 从链表中删除该节点
            self.remove_node_from_list(node)
            # 把该节点添加到链表头部
            self.push_node_to_front(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node_from_list(self.cache[key])

        node = ListNode(key, value)
        self.cache[key] = node
        self.push_node_to_front(node)

        if len(self.cache) > self.cap:
            last_node = self.tail.prev
            self.remove_node_from_list(last_node)
            self.cache.pop(last_node.key)
        return

    def remove_node_from_list(self, node) -> None:
        pre = node.prev
        nxt = node.next
        pre.next, nxt.prev = nxt, pre

    def push_node_to_front(self, node) -> None:
        nxt = self.head.next
        self.head.next, node.prev = node, self.head
        node.next, nxt.prev = nxt, node

