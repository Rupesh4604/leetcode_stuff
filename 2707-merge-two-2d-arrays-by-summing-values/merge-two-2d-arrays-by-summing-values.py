class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ds = dict()
        res = []

        for element in nums1:
            ds[element[0]] = element[1]

        ds = {element[0]: element[1] for element in nums1}

        for pair in nums2:
            ds[pair[0]] = ds.get(pair[0], 0) + pair[1] 

        res = [[k, v] for k, v in ds.items()] 
        res.sort(key=lambda x: x[0])

        return res