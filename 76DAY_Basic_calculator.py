# Stack approach
class Solution(object):
    def calculate(self, s):
        stack = []
        result = 0
        current_number = 0
        sign = 1
        
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '+':
                result += sign * current_number
                current_number = 0
                sign = 1
            elif char == '-':
                result += sign * current_number
                current_number = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * current_number
                current_number = 0
                result *= stack.pop()  # pop the sign
                result += stack.pop()  # pop the previous result
        return result + sign * current_number
        
# recursive approach
class Solution:
    def calculate(self, s) :
        def helper(i):
            result = 0
            sign = 1
            current_number = 0
            
            while i < len(s):
                char = s[i]
                if char.isdigit():
                    current_number = current_number * 10 + int(char)
                elif char == '+':
                    result += sign * current_number
                    current_number = 0
                    sign = 1
                elif char == '-':
                    result += sign * current_number
                    current_number = 0
                    sign = -1
                elif char == '(':
                    current_number, i = helper(i + 1)
                elif char == ')':
                    result += sign * current_number
                    return result, i
                i += 1
            
            result += sign * current_number
            return result, i
        
        return helper(0)[0]
