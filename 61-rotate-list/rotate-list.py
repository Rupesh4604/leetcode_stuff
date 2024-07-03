# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None or k==0:
            return head

        temp = head
        length = 1
        while temp.next is not None:
            temp = temp.next
            length +=1
        temp.next = head

        k = k%length
        N = length - k
        while N:
            temp = temp.next 
            N-=1
        head = temp.next 
        temp.next = None 
        return head
