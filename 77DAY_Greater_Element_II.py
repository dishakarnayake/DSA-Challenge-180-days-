# brute force 
class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        for i in range(n):
            for j in range(1, n):
                if nums[(i + j) % n] > nums[i]:
                    res[i] = nums[(i + j) % n]
                    break
        return res
        
# stack approach
class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
        
        return res


# deque 
from collections import deque

class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        dq = deque()

        for i in range(2 * n):
            while dq and nums[dq[-1]] < nums[i % n]:
                res[dq.pop()] = nums[i % n]
            if i < n:
                dq.append(i)
        
        return res
