class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = list(map(int, version1.split('.')))
        arr2 = list(map(int, version2.split('.')))
        if len(arr1)<len(arr2):
            maxl = len(arr1) 
        else:
            maxl = len(arr2)

        for i in range(maxl):
            if arr1[i]>arr2[i]:
                return 1
            elif arr1[i]<arr2[i]:
                return -1
            else:
                pass

        if len(arr1)<len(arr2):
            for j in range(maxl,len(arr2)):
                if arr2[j]>0:
                    return -1
            return 0
        if len(arr1)>len(arr2):
            for j in range(maxl,len(arr1)):
                if arr1[j]>0:
                    return 1
            return 0    
        return 0