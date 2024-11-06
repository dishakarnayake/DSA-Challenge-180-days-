class Solution:
    def findCircleNum(self, isConnected):
        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        n = len(isConnected)
        visited = set()
        provinces = 0

        for city in range(n):
            if city not in visited:
                provinces += 1
                visited.add(city)
                dfs(city)
        
        return provinces


from collections import deque

class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                provinces += 1
                queue = deque([i])
                
                while queue:
                    city = queue.popleft()
                    visited[city] = True
                    for neighbor in range(n):
                        if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                            queue.append(neighbor)
        
        return provinces
