# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        left = head
        right = head
        pairs = []
        while right.next:
            right = right.next
        while left != right and left.prev != right:
            total = left.data + right.data
            if total == target:
                pairs.append([left.data,right.data])
                left = left.next
                right = right.prev
            elif total < target:
                left = left.next
            else:
                right = right.prev
        return pairs