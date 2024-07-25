# Approach : Brute Force Method
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = int(a,2)
        y = int(b,2)
        z = x+y
        z = bin(z)[2:]
        return z
        
a = "1010"
b = "1011"
res = Solution().addBinary(a,b)
print(res)
# time complexity O(n)
# space complexity O(n)





# Approach : Two Pointer
class solution:
        def addBinary(self, a, b) :
            s = []
            carry = 0
            i = len(a) - 1
            j = len(b) - 1

            while i >= 0 or j >= 0 or carry:
                if i >= 0:
                    carry += int(a[i])
                    i -= 1
                if j >= 0:
                    carry += int(b[j])
                    j -= 1
                s.append(str(carry % 2))
                carry //= 2

            return ''.join(reversed(s))
# time complexity O(n)
# space complexity O(n)