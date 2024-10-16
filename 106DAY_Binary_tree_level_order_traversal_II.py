from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.insert(0, level_nodes)
        
        return result









class Solution(object):
    def levelOrderBottom(self, root):
        result = []
        
        def dfs(node, depth):
            if not node:
                return
            
            if depth == len(result):
                result.append([])  
            
            result[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return result[::-1] 








from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        
        stack = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            stack.append(level_nodes)  
            
        return stack[::-1]  
