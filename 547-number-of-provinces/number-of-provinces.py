class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        provinces = 0
        
        for i in range(n):
            if not visited[i]:
                provinces +=1
                q = deque([i])
                visited[i]=1

                while q:
                    city = q.popleft()
                    for neigh in range(n):
                        if isConnected[city][neigh]==1 and not visited[neigh]:
                            visited[neigh]=1
                            q.append(neigh)
        return provinces