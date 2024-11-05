import heapq

from typing import List
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        visited = [False] * V
        # Min-heap to select the edge with minimum weight.
        min_heap = [(0, 0)]  # (weight, vertex)
        total_weight = 0
        
        while min_heap:
            weight, u = heapq.heappop(min_heap)
            # If the node is already visited, skip it.
            if visited[u]:
                continue
            
            # Mark the node as visited and add its weight to the total weight.
            visited[u] = True
            total_weight += weight
            
            # Add all adjacent edges of u to the heap if the adjacent node is not visited.
            for neighbor in adj[u]:
                v, w = neighbor  # v is the adjacent node, w is the weight
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))
        
        return total_weight