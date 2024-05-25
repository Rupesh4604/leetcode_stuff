class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = float('-inf')
        pref = 1
        suff = 1
        n = len(nums)
        for i in range(n):
            if pref==0:
                pref=1
            if suff==0:
                suff=1
            pref *= nums[i]
            suff *= nums[n-i-1]
            maxprod = max(maxprod,max(pref,suff))
        return maxprod
        