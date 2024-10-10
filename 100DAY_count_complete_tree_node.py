class Solution:
    def countNodes(self, root):
        def height(node):
            if not node:
                return 0
            return 1 + height(node.left)

        if not root:
            return 0

        left_height = height(root.left)
        right_height = height(root.right)

        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right)
        else:
            return (1 << right_height) + self.countNodes(root.left)



class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        def get_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        def exists(idx, height, node):
            left, right = 0, (1 << (height - 1)) - 1
            for _ in range(height - 1):
                mid = (left + right) // 2
                if idx <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            return node is not None
        
        height = get_height(root)
        if height == 0:
            return 0
        
        left, right = 0, (1 << (height - 1)) - 1
        while left <= right:
            mid = (left + right) // 2
            if exists(mid, height, root):
                left = mid + 1
            else:
                right = mid - 1
        return (1 << (height - 1)) - 1 + left


class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
