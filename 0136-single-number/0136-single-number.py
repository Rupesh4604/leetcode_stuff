class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0 
        for elem in nums:
            xor ^= elem
        return xor