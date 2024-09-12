
# using  brute force method
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        for num in nums1:
            index = nums2.index(num)
            next_greater = -1
            for i in range(index + 1, len(nums2)):
                if nums2[i] > num:
                    next_greater = nums2[i]
                    break
            ans.append(next_greater)
        return ans
        
# using stack and hash map
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        return [next_greater.get(num, -1) for num in nums1]




