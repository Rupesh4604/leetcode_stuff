class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def countPaths(i, j, m, n, dp):
            if i==m-1 and j==n-1:
                return 1
            elif i>=m or j>=n:
                return 0
            elif dp[i][j]!=-1:
                return dp[i][j] 
            else:
                dp[i][j]=countPaths(i+1, j, m, n, dp) + countPaths(i, j+1, m, n, dp)
                return dp[i][j]
            
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        # dp[1][1]=1;
        num = countPaths(0, 0, m, n, dp)
        if m == 1 and n == 1:
            return num
        return dp[0][0]