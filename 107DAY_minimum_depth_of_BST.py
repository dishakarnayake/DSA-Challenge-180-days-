class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

from collections import deque

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        queue = deque([(root, 1)]) 
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))


class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        stack = [(root, 1)]
        min_depth = float('inf')
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                min_depth = min(min_depth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return min_depth
