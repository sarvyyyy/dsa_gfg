""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        temp = head
        while temp:
            next1 = temp.prev
            temp.prev = temp.next
            temp.next = next1
            head = temp
            temp = temp.prev
        return head
        