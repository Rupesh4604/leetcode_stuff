class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # as the loop produces only 0 to n-1 integers
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= i
        for num in nums:
            missing ^= num
        return missing

        
        