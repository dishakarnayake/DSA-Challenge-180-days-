# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        self.prev = None

        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)

        return inorder(root)


class Solution:
    def isValidBST(self, root):
        stack, prev = [], None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if prev is not None and root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True




  