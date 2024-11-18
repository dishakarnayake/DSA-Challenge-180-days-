class Solution(object):
    def swimInWater(self, grid):
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        min_heap = [(grid[0][0], 0, 0)]  # (elevation, x, y)
        visited[0][0] = True
        max_elevation = 0
        
        while min_heap:
            elevation, x, y = heapq.heappop(min_heap)
            max_elevation = max(max_elevation, elevation)
            
            # If we reach the bottom-right cell, return the result
            if x == n - 1 and y == n - 1:
                return max_elevation
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(min_heap, (grid[nx][ny], nx, ny))
