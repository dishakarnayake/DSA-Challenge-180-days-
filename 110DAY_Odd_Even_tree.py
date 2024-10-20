from collections import deque

class Solution(object):
    def isEvenOddTree(self, root):
        if not root:
            return True
        queue = deque([root])
        level = 0
        
        while queue:
            level_size = len(queue)
            prev_value = None
            for i in range(level_size):
                node = queue.popleft()
                
                if level % 2 == 0:
                    if node.val % 2 == 0 or (prev_value is not None and node.val <= prev_value):
                        return False
                else:
                    if node.val % 2 != 0 or (prev_value is not None and node.val >= prev_value):
                        return False
                
                prev_value = node.val  
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
        
        return True



class Solution(object):
    def isEvenOddTree(self, root):
        def dfs(node, level, prev_vals):
            if not node:
                return True
            
            if level % 2 == 0:
                if node.val % 2 == 0 or (level in prev_vals and node.val <= prev_vals[level]):
                    return False
            else:
                if node.val % 2 != 0 or (level in prev_vals and node.val >= prev_vals[level]):
                    return False
            
            prev_vals[level] = node.val
            
            return dfs(node.left, level + 1, prev_vals) and dfs(node.right, level + 1, prev_vals)
        
        prev_vals = {}
        return dfs(root, 0, prev_vals)
