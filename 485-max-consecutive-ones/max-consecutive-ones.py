class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt += 1
                longest = max(longest,cnt)
            else:
                cnt = 0
        return longest