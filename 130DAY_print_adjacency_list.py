from typing import List


class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        adj_list = [[] for _ in range(V)]
        
        # Populate the adjacency list
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # Sort each adjacency list for a consistent order (optional based on requirements)
        for neighbors in adj_list:
            neighbors.sort()
        
        return adj_list
        


from typing import List, Dict

class Solution:
    def printGraph(self, V: int, edges: List[List[int]]) -> Dict[int, List[int]]:
        # Initialize adjacency dictionary
        adj_dict = {i: [] for i in range(V)}
        
        # Populate the adjacency dictionary
        for u, v in edges:
            adj_dict[u].append(v)
            adj_dict[v].append(u)
        
        # Sort each adjacency list for a consistent order (optional)
        for key in adj_dict:
            adj_dict[key].sort()
        
        return adj_dict