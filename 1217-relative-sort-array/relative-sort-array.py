from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        res = []
        for elem in arr2:
            res.extend([elem] * count[elem])
            del count[elem]

        # Adding the remaining elements at the end
        remaining = sorted(count.elements())
        res.extend(remaining)
        
        return res
             