class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:-x[1])
        print(boxTypes)
        count = 0
        res = 0
        for i in range(len(boxTypes)):
            if count+boxTypes[i][0]<truckSize:
                res += (boxTypes[i][0]*boxTypes[i][1])
                count += boxTypes[i][0]
            else:
                res += (boxTypes[i][1]*(truckSize-count))
                return res
        return res
