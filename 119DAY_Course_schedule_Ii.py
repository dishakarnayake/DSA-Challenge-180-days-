from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses, prerequisites):
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degree[dest] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        
        while queue:
            course = queue.popleft()
            order.append(course)
            
            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return order if len(order) == numCourses else []



class Solution:
    def findOrder(self, numCourses, prerequisites):
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        
        visited = [0] * numCourses
        order = []
        
        def dfs(course):
            if visited[course] == 1:  
                return False
            if visited[course] == 2: 
                return True
            
            visited[course] = 1
            for neighbor in adj_list[course]:
                if not dfs(neighbor):
                    return False
            
            visited[course] = 2
            order.append(course)
            return True
        
        for course in range(numCourses):
            if visited[course] == 0:
                if not dfs(course):
                    return []
        
        return order[::-1]
