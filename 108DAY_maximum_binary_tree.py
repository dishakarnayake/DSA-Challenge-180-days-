class Solution:
    def constructMaximumBinaryTree(self, nums):
        stack = []

        for num in nums:
            curr_node = TreeNode(num)
 
            while stack and stack[-1].val < num:
                curr_node.left = stack.pop()
 
            if stack:
                stack[-1].right = curr_node
 
            stack.append(curr_node)

        return stack[0]

