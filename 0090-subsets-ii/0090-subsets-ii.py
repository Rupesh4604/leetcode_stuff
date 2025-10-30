class Solution:
    def helper(self,idx,nums,n,dp,ans):
            if idx==n:
                dp.sort()
                ans.add(tuple(dp[:]))
                return ans
            dp.append(nums[idx])
            self.helper(idx+1,nums,n,dp,ans)
            dp.pop()
            self.helper(idx+1,nums,n,dp,ans)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        dp = []
        ans = set()
        n = len(nums)
        nums.sort()
        self.helper(0,nums,n,dp,ans)
        return ans