class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxi = summ = nums[0]
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                summ += nums[i+1]
            else:
                summ = nums[i+1]
            maxi = max(summ,maxi)
        return maxi