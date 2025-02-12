class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        icx = 1
        maxi=0
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                icx += 1
            else:
                icx = 1
            maxi = max(maxi,icx)
        
        dcx = 1
        mini = 0
        for i in range(n-1):
            if nums[i]<nums[i+1]:
                dcx +=1
            else:
                dcx = 1
            mini = max(mini,dcx)
        
        return max(maxi,mini,1)

