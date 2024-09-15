
# stack based approach
class Solution(object):
    def calPoints(self, operations):
        stack = []
        
        for op in operations:
            if op == 'C':
                stack.pop()  # Invalidate the last score
            elif op == 'D':
                stack.append(2 * stack[-1])  # Double the last score
            elif op == '+':
                stack.append(stack[-1] + stack[-2])  # Sum of the last two scores
            else:
                stack.append(int(op))  # Add the integer score
        
        return sum(stack)

        
# two pointer simulation
class Solution(object):
    def calPoints(self, operations):
        points = [0] * len(operations)
        index = -1
        
        for op in operations:
            if op == 'C':
                index -= 1  # Invalidate the previous score
            elif op == 'D':
                points[index + 1] = 2 * points[index]  # Double the last score
                index += 1
            elif op == '+':
                points[index + 1] = points[index] + points[index - 1]  # Sum of the last two scores
                index += 1
            else:
                index += 1
                points[index] = int(op)  # Record the new score
        
        return sum(points[:index + 1])


# using list comprehension
class Solution(object):
    def calPoints(self, operations):
        stack = []
        ops_map = {
            'C': lambda: stack.pop(),
            'D': lambda: stack.append(stack[-1] * 2),
            '+': lambda: stack.append(stack[-1] + stack[-2])
        }
        
        for op in operations:
            if op in ops_map:
                ops_map[op]()
            else:
                stack.append(int(op))
        
        return sum(stack)
