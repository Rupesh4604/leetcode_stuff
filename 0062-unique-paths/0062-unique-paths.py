class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def countPaths(i, j, m, n):
            if i==m-1 and j==n-1:
                return 1
            elif i>=m or j>=n:
                return 0
            else:
                return countPaths(i+1, j, m, n) + countPaths(i, j+1, m, n)
            
        return countPaths(0,0,m,n)