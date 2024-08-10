# iterative counting
class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0
        max_depth = 0
        
        for char in s:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        
        return max_depth


# Stack based approach
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0
        
        for char in s:
            if char == '(':
                stack.append(char)
                max_depth = max(max_depth, len(stack))
            elif char == ')':
                stack.pop()
        
        return max_depth
