#optimal approach using two pointer python
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            print(0)

        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1
    
    
    
# brute force method python
class solution:
    def removeDuplicates(self, nums):
        k = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k