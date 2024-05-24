class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = 0
        ds = defaultdict(int)
        count = 0
        ds[0]=1
        for i in range(len(nums)):
            preSum += nums[i]
            diff = preSum - k
            count += ds[diff]
            ds[preSum] = ds.get(preSum,0)+1
        return count

