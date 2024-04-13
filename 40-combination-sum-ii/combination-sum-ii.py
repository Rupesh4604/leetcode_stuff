class Solution:
    def __init__(self):
        self.result = [] 

    def solve(self, candidates, target, index, ds):
        if target == 0:
            self.result.append(ds[:])
            return
        if index == len(candidates) or target < candidates[index]:
            return

        temp = candidates[index]
        ds.append(candidates[index])  # Choose current element
        self.solve(candidates, target - candidates[index], index + 1, ds)
        ds.pop()  # Backtrack: remove last element

        i = 1
        while index + i < len(candidates) and candidates[index + i] == temp:
            i += 1  # Skip duplicates
        self.solve(candidates, target, index + i, ds)  # Recur without choosing current element

    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.solve(candidates, target, 0, [])
        return self.result