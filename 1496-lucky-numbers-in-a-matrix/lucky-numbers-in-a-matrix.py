class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows = len(matrix)
        cols = len(matrix[0])
        for j in range(cols):
            max_row = 0
            for i in range(rows):
                if matrix[i][j]>matrix[max_row][j]:
                    max_row = i
            if matrix[max_row][j] == min(matrix[max_row]):
                res.append(matrix[max_row][j])
        return res