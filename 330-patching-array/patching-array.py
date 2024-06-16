class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        missing = 1
        i = 0
        
        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                # If the current number in nums can help cover the missing number
                missing += nums[i]
                i += 1
            else:
                # Add a patch to cover the missing number
                missing += missing
                patches += 1
        
        return patches
        
        # def combinationsum(idx, current_sum):
        #     if idx == len(nums):
        #         possible_sums.add(current_sum)
        #         return
        #     combinationsum(idx + 1, current_sum + nums[idx])
        #     combinationsum(idx + 1, current_sum)

        # # Initialize the set of possible sums
        # possible_sums = set()
        # combinationsum( 0, 0,)

        # patches = 0
        # for x in range(1, n + 1):
        #     if x not in possible_sums:
        #         patches += 1
        #         # Update possible sums with the new patch
        #         new_sums = set()
        #         for s in possible_sums:
        #             if s + x <= n:
        #                 new_sums.add(s + x)
        #         possible_sums.update(new_sums)
        #         possible_sums.add(x)   
        # return patches