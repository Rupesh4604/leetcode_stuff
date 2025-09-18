class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        # binary search
        low = 0
        high = m*n -1
        while low<=high:
            mid = (low+high)//2
            rows = mid//m
            cols = mid % m
            if matrix[rows][cols]==target:
                return True
            elif matrix[rows][cols]<target:
                low=mid+1
            else:
                high = mid-1
        return False 