# check suffix
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:  # Check if the digit is odd
                return num[:i+1]
        return ""

# Slicing string
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:  # Check if the digit is odd
                return num[:i+1]
        return ""