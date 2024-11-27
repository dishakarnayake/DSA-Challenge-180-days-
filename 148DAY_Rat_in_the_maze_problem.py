class Solution:
    # Function to find all possible paths
    def findPath(self, mat):
        n = len(mat)
        if mat[0][0] == 0 or mat[n-1][n-1] == 0:
            return []

        directions = {'D': (1, 0), 'U': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
        result = []

        def backtrack(x, y, path):
            if x == n-1 and y == n-1:  # Destination reached
                result.append(path)
                return

            for move, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and mat[nx][ny] == 1:
                    mat[nx][ny] = 0  # Mark as visited
                    backtrack(nx, ny, path + move)
                    mat[nx][ny] = 1  # Unmark for backtracking

        mat[0][0] = 0  # Mark the starting cell as visited
        backtrack(0, 0, "")
        return sorted(result)