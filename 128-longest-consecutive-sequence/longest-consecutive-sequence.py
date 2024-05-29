class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        maxcount = 0
        
        for num in nums:
            if num - 1 not in numbers:
                current_num = num
                count = 1
                
                while current_num + 1 in numbers:
                    current_num += 1
                    count += 1
                    
                maxcount = max(maxcount, count)
                
        return maxcount
        
