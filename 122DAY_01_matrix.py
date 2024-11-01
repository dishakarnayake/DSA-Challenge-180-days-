import heapq

class Solution:
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        min_heap = []
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    heapq.heappush(min_heap, (0, r, c))  
                else:
                    mat[r][c] = float('inf')
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while min_heap:
            dist, r, c = heapq.heappop(min_heap)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] > dist + 1:
                    mat[nr][nc] = dist + 1
                    heapq.heappush(min_heap, (mat[nr][nc], nr, nc))
                    
        return mat



class Solution:
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] != 0:
                    top = mat[r - 1][c] if r > 0 else float('inf')
                    left = mat[r][c - 1] if c > 0 else float('inf')
                    mat[r][c] = min(top, left) + 1

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if mat[r][c] != 0:
                    bottom = mat[r + 1][c] if r < rows - 1 else float('inf')
                    right = mat[r][c + 1] if c < cols - 1 else float('inf')
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)
                    
        return mat


from collections import deque

class Solution:
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = float('inf')
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # BFS
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
        
        return mat
