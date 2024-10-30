class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        state = [0] * n  # 0: unvisited, 1: visiting, 2: safe
        
        def dfs(node):
            if state[node] != 0:
                return state[node] == 2  # return True if it's already determined as safe
            state[node] = 1  # mark as visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False  # if any neighbor leads to an unsafe path
            state[node] = 2  # mark as safe
            return True
        
        safe_nodes = [node for node in range(n) if dfs(node)]
        return sorted(safe_nodes)










from collections import deque, defaultdict

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        reverse_graph = defaultdict(list)
        out_degree = [0] * n
        
        # Reverse the graph and compute the out-degree of each node
        for src in range(n):
            for dst in graph[src]:
                reverse_graph[dst].append(src)
            out_degree[src] = len(graph[src])
        
        # Start with all terminal nodes (out_degree == 0)
        queue = deque([node for node in range(n) if out_degree[node] == 0])
        safe_nodes = []
        
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for predecessor in reverse_graph[node]:
                out_degree[predecessor] -= 1
                if out_degree[predecessor] == 0:
                    queue.append(predecessor)
        
        return sorted(safe_nodes)
