# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result = []
        self.helper(root, result)
        return result
    
    def helper(self, node, result):
        if node:
            self.helper(node.left, result)  
            result.append(node.val)        
            self.helper(node.right, result)
        







class Solution:
    def inorderTraversal(self, root):
        result, stack = [], []
        current = root
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            
            current = current.right
        
        return result







class Solution:
    def inorderTraversal(self, root):
        result = []
        current = root
        
        while current:
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right
        
        return result
