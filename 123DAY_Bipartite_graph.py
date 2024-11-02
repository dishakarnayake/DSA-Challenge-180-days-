class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n  # -1 means uncolored

        def dfs(node, c):
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor] == -1:  # not colored
                    if not dfs(neighbor, 1 - c):  # Alternate color
                        return False
                elif color[neighbor] == color[node]:  # Same color as current node
                    return False
            return True

        for i in range(n):
            if color[i] == -1:  # Not visited
                if not dfs(i, 0):
                    return False
        return True







from collections import deque

class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n  # -1 means uncolored

        for i in range(n):
            if color[i] == -1:  # Not visited
                queue = deque([i])
                color[i] = 0
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if color[neighbor] == -1:  # Not colored
                            color[neighbor] = 1 - color[node]
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:  # Same color as current node
                            return False
        return True
