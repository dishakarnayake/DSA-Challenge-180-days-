# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val
        
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)












class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        stack = [(root, targetSum - root.val)]
        
        while stack:
            current, current_sum = stack.pop()
            if not current.left and not current.right and current_sum == 0:
                return True

            if current.left:
                stack.append((current.left, current_sum - current.left.val))
            if current.right:
                stack.append((current.right, current_sum - current.right.val))
        
        return False








from collections import deque


class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        queue = deque([(root, targetSum - root.val)])
        
        while queue:
            current, current_sum = queue.popleft()
            
            if not current.left and not current.right and current_sum == 0:
                return True
            
            if current.left:
                queue.append((current.left, current_sum - current.left.val))
            if current.right:
                queue.append((current.right, current_sum - current.right.val))
        
        return False
