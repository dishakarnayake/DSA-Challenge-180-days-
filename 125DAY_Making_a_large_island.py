class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        island_area = {} 
        island_id = 2  
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(x, y, island_id):
            if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != 1:
                return 0
            grid[x][y] = island_id
            area = 1
            for dx, dy in directions:
                area += dfs(x + dx, y + dy, island_id)
            return area

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_area[island_id] = dfs(i, j, island_id)
                    island_id += 1

        max_area = max(island_area.values()) if island_area else 0
 
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
               
                    seen_islands = set()
                    area = 1 
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            island_id = grid[ni][nj]
                            if island_id not in seen_islands:
                                area += island_area[island_id]
                                seen_islands.add(island_id)
                    max_area = max(max_area, area)

        return max_area
