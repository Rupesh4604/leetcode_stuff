# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB
        while temp1!=temp2:
            temp1 = headB if temp1==None else temp1.next
            temp2 = headA if temp2==None else temp2.next 
        return temp1
            