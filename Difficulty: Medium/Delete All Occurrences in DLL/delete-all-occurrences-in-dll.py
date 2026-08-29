"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""
class Solution:
    def deleteAllOccurOfX(self, head, x):
        temp = head
        while temp:
            if temp.data == x:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
            temp = temp.next
        return head