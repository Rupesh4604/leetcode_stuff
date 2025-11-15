class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        preCol = image[sr][sc]
        if preCol==color:
            return image
        
        image[sr][sc]=color

        q = deque([(sr,sc)])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while q:
            r,c = q.popleft()
            for dx,dy in directions:
                x,y = r+dx,c+dy
                if 0<=x<m and 0<=y<n and image[x][y]==preCol:
                    image[x][y]=color
                    q.append((x,y))
        return image
                