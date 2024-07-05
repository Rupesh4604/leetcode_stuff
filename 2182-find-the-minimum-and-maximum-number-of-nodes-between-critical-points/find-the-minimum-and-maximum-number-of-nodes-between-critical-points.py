# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        front = curr.next
        count = 1
        arr = []
        while front:
            if curr.val>prev.val and curr.val>front.val:
                arr.append(count)
            elif curr.val<prev.val and curr.val<front.val:
                arr.append(count)
            front = front.next
            curr = curr.next
            prev = prev.next
            count += 1 
        if len(arr)<2:
            return [-1,-1]
        elif len(arr)==2:
            return [arr[-1]-arr[0],arr[-1]-arr[0]]
        max_distance = arr[-1]-arr[0]
        min_distance = float(inf)
        for i in range(1,len(arr)):
            min_distance = min(min_distance, arr[i]-arr[i-1])
        return [min_distance,max_distance]


