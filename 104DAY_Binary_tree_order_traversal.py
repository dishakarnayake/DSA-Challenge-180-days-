from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])  
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()  
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)  
        
        return result




class Solution:
    def levelOrder(self, root):
        result = []
        self._dfs(root, 0, result)
        return result
    
    def _dfs(self, node, level, result):
        if not node:
            return
        
        if len(result) == level:
            result.append([])
        
        result[level].append(node.val)
        
        self._dfs(node.left, level + 1, result)
        self._dfs(node.right, level + 1, result)










class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        result = []
        stack = [(root, 0)]  
        
        while stack:
            node, level = stack.pop()
            
            if len(result) == level:
                result.append([])
            
            result[level].append(node.val)
            
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        
        return result

        