# Approach 1
# iterative
class Solution:
    def largestOddNumber(self, num):
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2:
                return num[:i + 1]

        return ""
# time complexity O(N)
# space complexity O(1)


# Approach 2
# iterate in reverse order
class Solution:
    def largestOddNumber(self, num):
        n = len(num)
        for i in range(n-1,-1,-1):
            if num[i]=='1' or num[i]=='3' or num[i]=='5' or num[i]=='7' or num[i]=='9':
                return num[:i+1]
        return ""

# time complexity O(N)
# space complexity O(1)
