class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort the list in-place based on squared Euclidean distance
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        return points[:k]