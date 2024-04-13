class Solution:
    def check(self, nums: List[int]) -> bool:
        breakpoints = 0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                breakpoints += 1
        if nums[len(nums)-1]>nums[0]:
            breakpoints +=1
        if breakpoints==1 or breakpoints==0:
            return True
        else:
            return False
        
                