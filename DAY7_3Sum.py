# brute force method looping
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        triplets = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets.append([nums[i], nums[j], nums[k]])
        return triplets
            
# using two pointer optimal approach
class solution:
    def threeSum(self, nums):
       
            nums.sort()
            triplets = []
            for i in range(len(nums) - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                left, right = i + 1, len(nums) - 1
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if total < 0:
                        left += 1
                    elif total > 0:
                        right -= 1
                    else:
                        triplets.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
            return triplets