class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        if target<nums[0]:
            return 0
        # elif target>nums[len(nums)-1]:
        #     return len(nums)
        while left<=right:
            mid = (left + right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return left
