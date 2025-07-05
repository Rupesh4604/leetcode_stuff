from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ds = Counter(arr)
        ans = 0
        for item, count in ds.items():
            if item==count:
                ans = max(ans,item)
        return ans if ans else -1