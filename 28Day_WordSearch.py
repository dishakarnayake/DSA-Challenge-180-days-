# using dfs approach
class Solution:
    def exist(self, board, word) :
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False
    
    def dfs(self, board, word, i, j, s) :
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
            return False
        if board[i][j] != word[s] or board[i][j] == '*':
            return False
        if s == len(word) - 1:
            return True
        
        cache = board[i][j]
        board[i][j] = '*'
        is_exist = self.dfs(board, word, i + 1, j, s + 1) or \
                   self.dfs(board, word, i - 1, j, s + 1) or \
                   self.dfs(board, word, i, j + 1, s + 1) or \
                   self.dfs(board, word, i, j - 1, s + 1)
        board[i][j] = cache
        
        return is_exist



# using backtracking
class solution:
    def exist(self, board, word):
        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = ''
            
            if backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1):
                return True
            
            board[i][j] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False
