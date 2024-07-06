# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = 0
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        
        def reverse(head):
            temp = head
            prev = None 
            while temp:
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front
            return prev
        new = reverse(mid)
        curr = new 
        temp2 = head
        while curr:
            res = max(res,curr.val+temp2.val)
            curr = curr.next
            temp2 = temp2.next
        return res
