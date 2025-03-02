class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ds = dict()
        res = []

        for element in nums1:
            ds[element[0]] = element[1]
        
        for pair in nums2:
            if pair[0] in ds:
                ds[pair[0]] += pair[1]
            else:
                ds[pair[0]] = pair[1] 
        
        [ res.append([k,v]) for k,v in ds.items()]

        res.sort(key=lambda x: x[0])

        return res