class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        #collect initial rotten oranges + count fresh ones
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))  # (row, col, minute)
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        directions = [(0,1),(-1,0),(1,0),(0,-1)]
        max_time = 0

        while q:
            r,c,t = q.popleft()
            max_time =  max(max_time,t)

            for dx,dy in directions:
                nr,nc = r+dx, c+dy
                if 0<=nr<n and 0<=nc<m and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    fresh -=1
                    q.append((nr,nc,t+1))
        
        return max_time if not fresh else -1