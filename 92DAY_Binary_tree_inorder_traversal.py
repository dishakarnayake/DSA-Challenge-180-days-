class Solution(object):
    def preorderTraversal(self, root):
        def dfs(node):
            if not node:
                return
            result.append(node.val)  # Visit root
            dfs(node.left)  # Traverse left
            dfs(node.right)  # Traverse right
        
        result = []
        dfs(root)
        return result


class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)  # Visit root
            
            if node.right:  # Push right first (so left is processed first)
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result



class Solution(object):
    def preorderTraversal(self, root):
        result = []
        current = root
        
        while current:
            if not current.left:
                result.append(current.val)  # Visit root
                current = current.right
            else:
                # Find the inorder predecessor of current
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                # Make current the right child of its inorder predecessor
                if not predecessor.right:
                    result.append(current.val)  # Visit root
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    current = current.right
        
        return result

