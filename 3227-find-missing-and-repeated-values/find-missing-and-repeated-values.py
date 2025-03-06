class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        size = n * n
        arr = [x for x in range(1,size+1)]
        a = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] in arr:
                    arr.remove(grid[i][j])
                else:
                    a = grid[i][j]
        return [a, arr[0]]
