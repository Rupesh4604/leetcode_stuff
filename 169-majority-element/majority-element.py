class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[len(nums)//2]
        n = len(nums)
        cnt = 0  # Count
        el = None  # Element

        # Moore’s Voting Algorithm
        for i in range(n):
            if cnt == 0:
                cnt = 1
                el = nums[i]
            elif el == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        
        if cnt>=1:
            return el
        return -1
        