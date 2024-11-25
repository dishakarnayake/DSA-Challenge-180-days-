class Solution:
    def solveNQueens(self, n):
        def is_valid(board, row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i][j] == 'Q':
                    return False
            return True
        def backtrack(board, row):
            if row == n:
                result.append([''.join(row) for row in board])
                return
            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row + 1)
                    board[row][col] = '.'
        result = []
        board = [['.'] * n for _ in range(n)]
        backtrack(board, 0)
        return result





class Solution:
    def solveNQueens(self, n):
        def backtrack(row):
            if row == n:
                result.append([''.join(board[i]) for i in range(n)])
                return
            for col in range(n):
                if col_used[col] or diag1_used[row - col] or diag2_used[row + col]:
                    continue
                board[row][col] = 'Q'
                col_used[col] = diag1_used[row - col] = diag2_used[row + col] = True
                backtrack(row + 1)
                board[row][col] = '.'
                col_used[col] = diag1_used[row - col] = diag2_used[row + col] = False
        result = []
        board = [['.'] * n for _ in range(n)]
        col_used = [False] * n
        diag1_used = [False] * (2 * n - 1)
        diag2_used = [False] * (2 * n - 1)
        backtrack(0)
        return result






class Solution:
    def solveNQueens(self, n):
        def backtrack(row, cols, diags1, diags2, current):
            if row == n:
                result.append([''.join(row) for row in current])
                return
            
            available_positions = (~(cols | diags1 | diags2)) & ((1 << n) - 1)
            while available_positions:
                pos = available_positions & -available_positions
                available_positions &= available_positions - 1
                col = bin(pos - 1).count('1')
                current[row][col] = 'Q'
                backtrack(row + 1, cols | pos, (diags1 | pos) << 1, (diags2 | pos) >> 1, current)
                current[row][col] = '.'

        result = []
        current = [['.'] * n for _ in range(n)]
        backtrack(0, 0, 0, 0, current)
        return result


