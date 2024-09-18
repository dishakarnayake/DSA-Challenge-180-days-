#brute force method
class Solution:
    def nextGreaterElement(self, n) :
        str_n = list(str(n))
        target = n + 1
        
        while target <= 2**31 - 1:
            if sorted(str(target)) == sorted(str_n):
                return target
            target += 1
        
        return -1




# Next permutation algorithm
class Solution(object):
    def nextGreaterElement(self, n):
            digits = list(str(n))
            length = len(digits)
            
            # Step 1: Find the first decreasing element from the right
            i = length - 2
            while i >= 0 and digits[i] >= digits[i + 1]:
                i -= 1
            
            # If no such element is found, no larger permutation is possible
            if i == -1:
                return -1
            
            # Step 2: Find the smallest digit larger than digits[i] to swap with
            j = length - 1
            while digits[j] <= digits[i]:
                j -= 1
            
            # Step 3: Swap digits[i] and digits[j]
            digits[i], digits[j] = digits[j], digits[i]
            
            # Step 4: Reverse the digits after index i
            digits = digits[:i+1] + digits[i+1:][::-1]
            
            result = int(''.join(digits))
            
            # Check if result fits a 32-bit integer
            return result if result <= 2**31 - 1 else -1
            