from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed_courses = 0

        while queue:
            course = queue.popleft()
            completed_courses += 1

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return completed_courses == numCourses








class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:
                return False 
            if visited[course] == 2:
                return True  
            visited[course] = 1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            visited[course] = 2
            return True

        for course in range(numCourses):
            if visited[course] == 0:
                if not dfs(course):
                    return False

        return True

