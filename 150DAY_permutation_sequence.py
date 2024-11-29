from itertools import permutations

class Solution:
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]
        all_permutations = list(permutations(nums))
        return ''.join(all_permutations[k - 1])



class Solution:
    def getPermutation(self, n, k):
        # Step 1: Create a list of numbers and factorials
        nums = [str(i) for i in range(1, n + 1)]
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i
        
        # Step 2: Convert k to zero-based index
        k -= 1
        result = []
        
        # Step 3: Find each digit of the kth permutation
        for i in range(n, 0, -1):
            index = k // factorial[i - 1]
            result.append(nums.pop(index))
            k %= factorial[i - 1]
        
        return ''.join(result)



class Solution:
    def getPermutation(self, n, k):
        def helper(nums, k, factorial):
            if not nums:
                return ""
            n = len(nums)
            index = k // factorial[n - 1]
            return nums.pop(index) + helper(nums, k % factorial[n - 1], factorial)
        
        nums = [str(i) for i in range(1, n + 1)]
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i
        
        k -= 1
        return helper(nums, k, factorial)
