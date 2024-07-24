
# Using four pointer
def spiralOrder(matrix):
    if not matrix:
        return []
    
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))




# Using directions
def SpiralOrder(matrix):
    if not matrix:
        return []
    
    result = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    dir_index = 0
    row, col = 0, 0
    
    for _ in range(len(matrix) * len(matrix[0])):
        result.append(matrix[row][col])
        matrix[row][col] = None
        
        next_row, next_col = row + directions[dir_index][0], col + directions[dir_index][1]
        if (next_row < 0 or next_row >= len(matrix) or next_col < 0 or next_col >= len(matrix[0]) or
                matrix[next_row][next_col] is None):
            dir_index = (dir_index + 1) % 4
            next_row, next_col = row + directions[dir_index][0], col + directions[dir_index][1]
        
        row, col = next_row, next_col
    
    return result

print(SpiralOrder([[1,2,3],[4,5,6],[7,8,9]]))


# Using single pass
def s_piralOrder(matrix):
    if not matrix:
        return []
    
    result = []
    def spiral(matrix, top, bottom, left, right):
        if top > bottom or left > right:
            return
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        
        spiral(matrix, top, bottom, left, right)
    
    spiral(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1)
    return result

print(s_piralOrder([[1,2,3],[4,5,6],[7,8,9]]))