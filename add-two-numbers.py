"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def parse_number(l):
    if l.next is None:
        return str(l.val)
    else:
        return parse_number(l.next) + str(l.val)


def manipulate_ln(n):
    ln_list = [ListNode(int(x)) for x in n][::-1]
    for index, value in enumerate(ln_list):
        if index == len(ln_list) - 1:
            break
        else:
            value.next = ln_list[index + 1]
    return ln_list[0]


def add_two_numbers(l1, l2):
    result = int(parse_number(l1)) + int(parse_number(l2))
    return manipulate_ln(str(result))


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
print(parse_number(l1))


l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(parse_number(l2))

print(parse_number(add_two_numbers(l1, l2)))

