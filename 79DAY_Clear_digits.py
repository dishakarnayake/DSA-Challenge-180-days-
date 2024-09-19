
# stack based
class Solution(object):
    def clearDigits(self, s):
        stack = []  # To store non-digit characters

        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()  # Remove the closest non-digit character
            else:
                stack.append(char)  # Push non-digit character to stack
        
        # Join the stack to form the final string
        return ''.join(stack)

# two pointer approach 
class Solution(object):
    def clearDigits(self, s):
        s = list(s)  # Convert string to list for easy mutation
        n = len(s)
        i = 0
        
        while i < n:
            if s[i].isdigit():
                # Remove the digit
                s[i] = ''
                
                # Find the closest non-digit character to the left
                j = i - 1
                while j >= 0 and s[j] == '':
                    j -= 1
                
                # Remove the non-digit character if it exists
                if j >= 0 and not s[j].isdigit():
                    s[j] = ''
            i += 1
        
        # Join the string and return the result
        return ''.join(s)
