class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ds = dict()
        ans = 0
        nums.sort()
        for i in nums:
            if (-i in ds) and i>ans:
                ans = i
            else:
                ds[i] = True
        if ans==0:
            return -1
        else:
            return ans
