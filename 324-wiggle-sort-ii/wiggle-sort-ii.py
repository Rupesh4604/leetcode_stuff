class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        
        # split into two halves
        mid = (n + 1) // 2
        small = nums[:mid][::-1]  # reverse smaller half
        large = nums[mid:][::-1]  # reverse larger half
        
        # fill even and odd positions
        nums[::2] = small
        nums[1::2] = large
        