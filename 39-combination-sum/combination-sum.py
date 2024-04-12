class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = []
        ans = []

        def combinationSumHelper(idx,target):
            if idx==len(candidates):
                if target == 0:
                    ans.append(dp[:])
                return
            if target<0:
                return
            dp.append(candidates[idx])
            combinationSumHelper(idx,target-candidates[idx])
            dp.pop()
            combinationSumHelper(idx+1,target)

        combinationSumHelper(0,target)
        return ans