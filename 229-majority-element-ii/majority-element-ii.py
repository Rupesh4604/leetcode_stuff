class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        majority_count = len(nums) // 3
        majority_elements = [num for num, count in counts.items() if count > majority_count]
        return majority_elements