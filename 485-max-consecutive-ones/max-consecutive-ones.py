class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for elem in nums:
            if elem==1:
                count +=1
            else:
                count = 0
            res = max(res, count)
        return res 