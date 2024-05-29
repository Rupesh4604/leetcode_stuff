# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # we cannot access the previous node thus we copy the data of the next node to this and skip the next node, essentially reducing the length of linkedlist by one
        node.val = node.next.val
        node.next = node.next.next
        