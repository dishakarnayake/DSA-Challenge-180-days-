class Solution:
    def solveSudoku(self, board):
        def is_valid(board, row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False
            return True

        def backtrack(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in '123456789':
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                if backtrack(board):
                                    return True
                                board[row][col] = '.'
                        return False
            return True

        backtrack(board)




class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Initialize the sets with existing numbers in the board
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def backtrack(r, c):
            if r == 9:  # Finished all rows
                return True
            if c == 9:  # Move to the next row
                return backtrack(r + 1, 0)
            if board[r][c] != '.':  # Skip filled cells
                return backtrack(r, c + 1)

            for num in '123456789':
                box_idx = (r // 3) * 3 + (c // 3)
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                    # Place the number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)

                    # Recur
                    if backtrack(r, c + 1):
                        return True

                    # Undo the placement
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)

            return False

        backtrack(0, 0)
