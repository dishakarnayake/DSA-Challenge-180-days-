class Solution:
    def findCenter(self, edges):
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]



from collections import defaultdict

class Solution:
    def findCenter(self, edges):
        degree = defaultdict(int)
        
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            
            if degree[u] > 1:
                return u
            if degree[v] > 1:
                return v


class Solution:
    def findCenter(self, edges):
        adj_list = {}
        
        for u, v in edges:
            if u not in adj_list:
                adj_list[u] = 0
            if v not in adj_list:
                adj_list[v] = 0
            adj_list[u] += 1
            adj_list[v] += 1
            
        for node, count in adj_list.items():
            if count == len(edges):
                return node
