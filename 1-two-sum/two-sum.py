class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = dict()

        for i in range(len(nums)):
            compliment = target - nums[i] 
            if compliment in dt:
                return [dt[compliment],i]
            else:
                dt[nums[i]]=i
        
        return []
