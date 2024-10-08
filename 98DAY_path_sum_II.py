class Solution:
    def pathSum(self, root, targetSum):
        def dfs(node, currentPath, currentSum):
            if not node:
                return []
            currentPath.append(node.val)
            currentSum += node.val
            
            if not node.left and not node.right and currentSum == targetSum:
                result.append(list(currentPath))
                
            if node.left:
                dfs(node.left, currentPath, currentSum)
            if node.right:
                dfs(node.right, currentPath, currentSum)
            currentPath.pop()
        
        result = []
        dfs(root, [], 0)
        return result








class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return []
        
        stack = [(root, [root.val], root.val)]  # (node, path, sum)
        result = []
        
        while stack:
            node, path, currentSum = stack.pop()
            if not node.left and not node.right and currentSum == targetSum:
                result.append(path)
            if node.right:
                stack.append((node.right, path + [node.right.val], currentSum + node.right.val))
            
            if node.left:
                stack.append((node.left, path + [node.left.val], currentSum + node.left.val))
        return result






from collections import deque

class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return []
        
        queue = deque([(root, [root.val], root.val)])  # (node, path, sum)
        result = []
        
        while queue:
            node, path, currentSum = queue.popleft()
            if not node.left and not node.right and currentSum == targetSum:
                result.append(path)
            if node.left:
                queue.append((node.left, path + [node.left.val], currentSum + node.left.val))
            
            if node.right:
                queue.append((node.right, path + [node.right.val], currentSum + node.right.val))
        
        return result
