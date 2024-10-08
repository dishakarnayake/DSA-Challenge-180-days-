


# Brute force method
class Solution:
    def removeElement(self, nums,  val) :
        i = 0
        while i < len(nums):
            if nums[i] == val:
                # Shift elements to the left
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j + 1]
                nums.pop()  # Remove the last element
            else:
                i += 1
        return len(nums)
        
 
 
 
 
 
# Optimal approach using two pointer

def removeElement(self, nums, val):
    left, right = 0, len(nums) - 1
    while left <= right:
            if nums[left] == val:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1
            else:
                    left += 1
    return left
               
        
