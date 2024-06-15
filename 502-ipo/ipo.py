from collections import defaultdict
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Pair up capital and profits and sort by capital required
        projects = sorted(zip(capital, profits))
        
        max_heap = []
        index = 0
        n = len(profits)
        
        for _ in range(k):
            # Push all projects that can be started with current capital into the heap
            while index < n and projects[index][0] <= w:
                heapq.heappush(max_heap, -projects[index][1])  # Use negative to simulate max-heap
                index += 1
            
            # If no projects can be done with current capital, break
            if not max_heap:
                break
            
            # Choose the project with the maximum profit
            w += -heapq.heappop(max_heap)  # Add the max profit (note the negation)
        
        return w