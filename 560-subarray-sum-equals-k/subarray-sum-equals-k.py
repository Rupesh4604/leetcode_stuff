class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ds = defaultdict(int) # hashmap of prefixsum:count
        prefixSum = 0
        count = 0
        ds[0] = 1   # prefixsum=0 -> count=1
        for i in range(len(nums)):
            prefixSum += nums[i]
            diff =  prefixSum - k
            count += ds[diff] 
            ds[prefixSum] = ds.get(prefixSum,0) + 1 
        return count 