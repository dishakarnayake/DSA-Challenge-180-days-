class Solution(object):
    def recoverTree(self, root): 
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))   

        def inorder(node):
            if not node:
                return 
            inorder(node.left)
             
            if self.prev.val > node.val: 
                if not self.first:
                    self.first = self.prev
                    self.second = node
                else:
                    self.second = node
            self.prev = node
            
            inorder(node.right)
        
        inorder(root)
        
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val









class Solution(object):
    def recoverTree(self, root):
       
        first = second = prev = None
        current = root
        
        while current:
            if current.left is None:
                if prev and prev.val > current.val:
                    if not first:
                        first = prev
                        second = current
                    else:
                        second = current
                prev = current
                current = current.right
            else:
                pre = current.left
                while pre.right and pre.right != current:
                    pre = pre.right
                
                if pre.right is None:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    if prev and prev.val > current.val:
                        if not first:
                            first = prev
                            second = current
                        else:
                            second = current
                    prev = current
                    current = current.right
        
        if first and second:
            first.val, second.val = second.val, first.val
