class Solution:
    def criticalConnections(self, n, connections):
        def dfs(node, parent, discovery_time, low, graph, result, time):
            discovery_time[node] = low[node] = time
            time += 1
            for neighbor in graph[node]:
                if discovery_time[neighbor] == -1:  # If neighbor is not visited
                    dfs(neighbor, node, discovery_time, low, graph, result, time)
                    # Update the low-link value after visiting the neighbor
                    low[node] = min(low[node], low[neighbor])
                    # If the condition for a bridge is met
                    if low[neighbor] > discovery_time[node]:
                        result.append([node, neighbor])
                elif neighbor != parent:  # Back edge
                    low[node] = min(low[node], discovery_time[neighbor])

        # Build the graph
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        discovery_time = [-1] * n  
        low = [-1] * n  
        result = []
        time = 0

        
        dfs(0, -1, discovery_time, low, graph, result, time)
        return result


class Solution:
    def criticalConnections(self, n, connections):
        def is_connected(n, edges):
            parent = list(range(n))

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(x, y):
                px = find(x)
                py = find(y)
                if px != py:
                    parent[px] = py

            for a, b in edges:
                union(a, b)

            root = find(0)
            return all(find(i) == root for i in range(n))

        critical = []
        for i in range(len(connections)):
            remaining_edges = connections[:i] + connections[i + 1:]
            if not is_connected(n, remaining_edges):
                critical.append(connections[i])

        return critical

        