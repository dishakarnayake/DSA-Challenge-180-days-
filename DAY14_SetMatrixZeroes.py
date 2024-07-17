
# using extra space
class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        row_set = set()
        col_set = set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        for i in range(rows):
            for j in range(cols):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0
        return matrix

obj = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(obj.setZeroes(matrix))



# using first row and column as markers
class solution(object):
    def setZeroes(self, matrix):
     
        m, n = len(matrix), len(matrix[0])
        first_row_zero, first_col_zero = False, False
        
        # Mark the first row and column
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        # Mark the rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set the rows and columns to 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Set the first row and column to 0
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

        return matrix 

    
obj1 = solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(obj1.setZeroes(matrix))



# using single pass
class S_olution(object):
    def setZeroes(self, matrix):
     
      
            m, n = len(matrix), len(matrix[0])
            first_row_zero, first_col_zero = False, False
            
            # Set the rows and columns to 0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == 0:
                        if i == 0:
                            first_row_zero = True
                        if j == 0:
                            first_col_zero = True
                        if i!= 0:
                            matrix[i][0] = 0
                        if j!= 0:
                            matrix[0][j] = 0
            
            # Set the rows and columns to 0
            for i in range(1, m):
                for j in range(1, n):
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
            
            # Set the first row and column to 0
            if first_row_zero:
                for j in range(n):
                    matrix[0][j] = 0
            if first_col_zero:
                for i in range(m):
                    matrix[i][0] = 0

            return matrix

obj2 = S_olution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]