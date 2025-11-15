class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque()
        res = [[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    res[i][j] = 0
                    q.append((i, j))
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        while q:
            r,c = q.popleft()
            for dx,dy in directions:
                x,y = r+dx,c+dy
                if 0<=x<m and 0<=y<n and res[x][y]==-1:
                    res[x][y] = res[r][c] + 1 
                    q.append((x,y))
        return res

