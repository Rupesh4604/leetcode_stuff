class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        ds = dict()
        for elem in nums1:
            if elem in ds:
                ds[elem]+=1
            else:
                ds[elem] = 1
        for elem in nums2:
            if elem in ds:
                ds[elem]-=1
                res.append(elem)
                if ds[elem]==0:
                    del ds[elem]
        return res



