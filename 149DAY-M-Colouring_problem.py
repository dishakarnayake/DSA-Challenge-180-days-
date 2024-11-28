class Solution:
    def graphColoring(self, v, edges, m):
        # Create adjacency list
        graph = {i: [] for i in range(v)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Dynamic Programming table
        dp = {}

        def is_valid(mask, colors):
            for node in range(v):
                for neighbor in graph[node]:
                    if (mask & (1 << node)) and (mask & (1 << neighbor)) and colors[node] == colors[neighbor]:
                        return False
            return True

        def dfs(mask, colors):
            if mask == 0:
                return True
            if mask in dp:
                return dp[mask]

            for node in range(v):
                if mask & (1 << node):
                    for color in range(1, m + 1):
                        colors[node] = color
                        if dfs(mask ^ (1 << node), colors):
                            dp[mask] = True
                            return True
                        colors[node] = 0

            dp[mask] = False
            return False

        return dfs((1 << v) - 1, [0] * v)
