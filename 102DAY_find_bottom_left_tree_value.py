from collections import deque
class Solution(object):
    def findBottomLeftValue(self, root):
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val

class Solution(object):
    def findBottomLeftValue(self, root):
        self.max_depth = -1
        self.leftmost_value = None
        def dfs(node, depth):
            if not node:
                return
            if depth > self.max_depth:
                self.max_depth = depth
                self.leftmost_value = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return self.leftmost_value



class Solution(object):
    def findBottomLeftValue(self, root):
        
        def dfs(node, depth):
            if not node:
                return (None, depth)
            
            if not node.left and not node.right:
                return (node.val, depth)
            
            left_value, left_depth = dfs(node.left, depth + 1)
            right_value, right_depth = dfs(node.right, depth + 1)
            
            if left_depth >= right_depth:
                return (left_value, left_depth)
            else:
                return (right_value, right_depth)
        
        value, _ = dfs(root, 0)
        return value
