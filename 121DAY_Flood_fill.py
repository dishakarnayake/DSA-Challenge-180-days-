class Solution:
    def floodFill(self, image, sr, sc, color):
        # Get the original color of the starting pixel
        original_color = image[sr][sc]
        # If the color is the same, no change is needed
        if original_color == color:
            return image
        
        # Helper function to perform DFS
        def dfs(r, c):
            # Check bounds and color matching
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != original_color:
                return
            # Update the color
            image[r][c] = color
            # Recursively apply to neighbors
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Start the DFS
        dfs(sr, sc)
        return image




from collections import deque

class Solution:
    def floodFill(self, image, sr, sc, color):
        original_color = image[sr][sc]
        if original_color == color:
            return image
        
        # Initialize a queue with the starting point
        queue = deque([(sr, sc)])
        image[sr][sc] = color  # Start by changing the color of the starting point
        
        # Directions array for moving in 4 directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check bounds and if the color matches the original
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == original_color:
                    image[nr][nc] = color
                    queue.append((nr, nc))
        
        return image



class Solution:
    def floodFill(self, image, sr, sc, color):
        original_color = image[sr][sc]
        if original_color == color:
            return image
        
        stack = [(sr, sc)]
        
        while stack:
            r, c = stack.pop()
            if image[r][c] == original_color:
                image[r][c] = color
                # Push neighbors onto stack if within bounds
                if r + 1 < len(image): stack.append((r + 1, c))
                if r - 1 >= 0: stack.append((r - 1, c))
                if c + 1 < len(image[0]): stack.append((r, c + 1))
                if c - 1 >= 0: stack.append((r, c - 1))
        
        return image
