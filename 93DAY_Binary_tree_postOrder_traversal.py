class Solution(object):
    def postorderTraversal(self, root):
        def helper(node, result):
            if not node:
                return
            helper(node.left, result)
           
            helper(node.right, result)
            result.append(node.val)
        
        result = []
        helper(root, result)
        return result



class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        
        stack1 = [root]
        stack2 = []
        result = []
        
        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            
            if node.right:
                stack1.append(node.right)

        while stack2:
            result.append(stack2.pop().val)
        
        return result



class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        
        stack, result = [], []
        last_visited = None
        current = root
        
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek_node = stack[-1]
                
                if peek_node.right and last_visited != peek_node.right:
                    current = peek_node.right
                else:
                    result.append(peek_node.val)
                    last_visited = stack.pop()
                    
        return result
