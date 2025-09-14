class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for elem in nums:
            if elem==1:
                count +=1
            else:
                res = max(res, count) # runs only when case is true
                count = 0
            # res = max(res, count) # this runs O(n) times
        res = max(res, count)  # Runs only once to handle edge cases
        # example where the max ones are in the end with no break  
        return res 