from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for number,count in counts.items():
            if count>1:
                return True
        return False
