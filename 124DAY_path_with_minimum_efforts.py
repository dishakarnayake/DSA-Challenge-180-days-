from collections import deque

class Solution:
    def minimumEffortPath(self, heights):
        def canReachEnd(mid):
            rows, cols = len(heights), len(heights[0])
            visited = set()
            queue = deque([(0, 0)])
            visited.add((0, 0))
            
            while queue:
                x, y = queue.popleft()
                if (x, y) == (rows - 1, cols - 1):
                    return True
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                        if abs(heights[nx][ny] - heights[x][y]) <= mid:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
            return False
        
        left, right = 0, max(max(row) for row in heights) - min(min(row) for row in heights)
        while left < right:
            mid = (left + right) // 2
            if canReachEnd(mid):
                right = mid
            else:
                left = mid + 1
        return left





import heapq

class Solution:
    def minimumEffortPath(self, heights):
        rows, cols = len(heights), len(heights[0])
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        min_heap = [(0, 0, 0)]  # (effort, x, y)
        
        while min_heap:
            current_effort, x, y = heapq.heappop(min_heap)
            if (x, y) == (rows - 1, cols - 1):
                return current_effort
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    next_effort = max(current_effort, abs(heights[nx][ny] - heights[x][y]))
                    if next_effort < efforts[nx][ny]:
                        efforts[nx][ny] = next_effort
                        heapq.heappush(min_heap, (next_effort, nx, ny))
