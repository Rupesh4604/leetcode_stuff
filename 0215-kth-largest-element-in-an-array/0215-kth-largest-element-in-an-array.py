class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)      # Push element into heap
            if len(min_heap) > k:
                heapq.heappop(min_heap)        # Remove smallest element
        res = list(min_heap)
        res.sort()
        return res[0]