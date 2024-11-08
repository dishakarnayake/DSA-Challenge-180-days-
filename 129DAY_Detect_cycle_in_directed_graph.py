from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def dfs(self, node, adj, visited, recStack):
        visited[node] = True
        recStack[node] = True
        
        # Visit all the neighbors
        for neighbor in adj[node]:
            if not visited[neighbor]:  # if neighbor is not visited, do DFS
                if self.dfs(neighbor, adj, visited, recStack):
                    return True
            elif recStack[neighbor]:  # if neighbor is in recursion stack, cycle found
                return True
        
        recStack[node] = False  # remove node from recursion stack before backtracking
        return False
    
    # Function to detect cycle in a directed graph using DFS
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False] * V
        recStack = [False] * V
        
        # Perform DFS from each unvisited node
        for node in range(V):
            if not visited[node]:  # Start DFS if node hasn't been visited
                if self.dfs(node, adj, visited, recStack):
                    return True
        return False
        
        
        
        
from collections import deque
from typing import List

class Solution:
    
    # Function to detect cycle in a directed graph using Kahn's Algorithm
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        # Step 1: Calculate in-degrees of all vertices
        in_degree = [0] * V
        for i in range(V):
            for neighbor in adj[i]:
                in_degree[neighbor] += 1
        
        # Step 2: Initialize queue with all vertices having in-degree 0
        queue = deque([i for i in range(V) if in_degree[i] == 0])
        
        # Step 3: Process the nodes in topological order
        count = 0  # Counter for number of processed vertices
        while queue:
            node = queue.popleft()
            count += 1
            
            # Decrease in-degree for all neighbors of node
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: If count != V, it means there is a cycle
        return count != V