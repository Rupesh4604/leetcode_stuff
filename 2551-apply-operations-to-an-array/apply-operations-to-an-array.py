class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        
        while i<n-1:
            if nums[i]!=nums[i+1]:
                i+=1
            else:
                nums[i] *=2
                nums[i+1] = 0
                i +=2
        # Shift zeros to the end (in-place)
        non_zero_idx = 0
        
        # Move all non-zero elements to the front
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero_idx] = nums[i]
                non_zero_idx += 1
        
        # Fill the remaining positions with zeros
        for i in range(non_zero_idx, n):
            nums[i] = 0
        
        return nums