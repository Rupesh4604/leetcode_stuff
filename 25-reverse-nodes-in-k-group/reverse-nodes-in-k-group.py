# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        temp = head
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def getKthNode(self,temp, k):
        k -= 1
        while temp is not None and k > 0:
            k -= 1
            temp = temp.next
        return temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        revlast = None
        while temp:
            kThNode = self.getKthNode(temp, k)
            if kThNode is None:
                if prevLast:
                    prevLast.next = temp
                break
            # remeber the next node and break the link
            nextNode = kThNode.next
            kThNode.next = None

            self.reverse(temp)
            if temp == head: # at start 
                head = kThNode
            else:
                prevLast.next = kThNode # remember the last node
            prevLast = temp 
            temp = nextNode
        return head
