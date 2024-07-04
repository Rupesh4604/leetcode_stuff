# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        modify = head.next
        temp = modify

        while temp:
            amount = 0
            while temp.val!=0:
                amount +=temp.val
                temp = temp.next
            modify.val = amount
            temp = temp.next
            modify.next = temp
            modify = modify.next
        return head.next

