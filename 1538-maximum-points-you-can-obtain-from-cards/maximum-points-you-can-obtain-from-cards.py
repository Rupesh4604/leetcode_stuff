class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        # # leftbound = k-1     # starting to K size window 
        # # rightbound = len(cardPoints)-1
        # n = len(cardPoints)
        # maxi = 0
        # # while (leftbound>=0):
        # #     maxi = max(sum(cardPoints[:leftbound]+cardPoints[rightbound:]),maxi)
        # #     leftbound -=1
        # #     rightbound -=1
        # for i in range(k):
        #     checksum = sum(cardPoints[:k-i-1]+cardPoints[n-1-i:])
        #     maxi = max(checksum,maxi)
        # return maxi
        n = len(cardPoints)
        window_size = n - k
        total_sum = sum(cardPoints)
        min_subarray_sum = float('inf')
        
        if window_size == 0:
            return total_sum
        
        current_sum = sum(cardPoints[:window_size])
        min_subarray_sum = min(min_subarray_sum, current_sum)
        
        for i in range(window_size, n):
            current_sum += cardPoints[i] - cardPoints[i - window_size]
            min_subarray_sum = min(min_subarray_sum, current_sum)
        
        return total_sum - min_subarray_sum