class Solution:
    def printTree(self, root):
        def getHeight(node):
            if not node:
                return -1  
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        def fillMatrix(res, node, row, col, height):
            if not node:
                return
            res[row][col] = str(node.val)
            if node.left:
                fillMatrix(res, node.left, row + 1, col - 2**(height - row - 1), height)
            if node.right:
                fillMatrix(res, node.right, row + 1, col + 2**(height - row - 1), height)

        height = getHeight(root)
        rows = height + 1
        cols = 2**(height + 1) - 1
        res = [["" for _ in range(cols)] for _ in range(rows)]
        fillMatrix(res, root, 0, (cols - 1) // 2, height)
        
        return res
