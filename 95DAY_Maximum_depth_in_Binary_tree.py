# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
        
from collections import deque

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        queue = deque([(root, 1)])
        max_depth = 0
        while queue:
            node, depth = queue.popleft()
            if node:
                max_depth = max(max_depth, depth)
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
        return max_depth
