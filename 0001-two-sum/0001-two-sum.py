class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ds = {}
        for i in range(len(nums)):
            if target-nums[i] in ds.keys():
                return [i,ds[target-nums[i]]]
            else:
                ds[nums[i]] = i
        return [-1,-1]
