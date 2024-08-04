# using buildin function
class solution:
    def myAtoi(self, s: str) -> int:
        
   
            s = s.lstrip()  # Remove leading whitespace
            if not s:  # If string is empty after removing whitespace
                return 0

            sign = 1  # Default sign is positive
            if s[0] == '-':
                sign = -1
                s = s[1:]
            elif s[0] == '+':
                s = s[1:]

            num = 0
            for char in s:
                if not char.isdigit():  # If non-digit character is encountered
                    break
                num = num * 10 + int(char)

            num *= sign

            # Rounding to 32-bit signed integer range
            if num < -2**31:
                return -2**31
            elif num > 2**31 - 1:
                return 2**31 - 1
            else:
                return num

#Time Complexity: O(n), where n is the length of the input string.
#Space Complexity: O(1), as we only use a constant amount of space.





#using manual loop
class Solution:
    def myAtoi(self, s: str) -> int:


            s = s.lstrip()  # Remove leading whitespace
            if not s:  # If string is empty after removing whitespace
                return 0

            sign = 1  # Default sign is positive
            if s[0] == '-':
                sign = -1
                s = s[1:]
            elif s[0] == '+':
                s = s[1:]

            num = 0
            for char in s:
                if not char.isdigit():  # If non-digit character is encountered
                    break
                digit = ord(char) - ord('0')
                if num > (2**31 - 1 - digit) // 10:  # Check for overflow
                    return 2**31 - 1 if sign == 1 else -2**31
                num = num * 10 + digit

            num *= sign
            return num

#Time Complexity: O(n), where n is the length of the input string.
# Space Complexity: O(1), as we only use a constant amount of space.