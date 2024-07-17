
# Brute force  method
class Solution:
    def fourSum(self, nums, target) :
        nums.sort()
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for d in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[d] == target:
                            quadruplet = sorted([nums[i], nums[j], nums[k], nums[d]])
                            if quadruplet not in result:
                                result.append(quadruplet)
        return result






# Using two pointer approach
class solution:
    def fourSum(self, nums , target):
        nums.sort()
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left, right = j + 1, len(nums) - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum < target:
                        left += 1
                    elif current_sum > target:
                        right -= 1
                    else:
                        quadruplet = sorted([nums[i], nums[j], nums[left], nums[right]])
                        if quadruplet not in result:
                            result.append(quadruplet)
                        left += 1
                        right -= 1
        return result





# Hashing Approach

class S_olution:
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum_ij = nums[i] + nums[j]
                hash_table = {}
                for k in range(j + 1, len(nums)):
                    complement = target - sum_ij - nums[k]
                    if complement in hash_table:
                        quadruplet = sorted([nums[i], nums[j], nums[k], complement])
                        if quadruplet not in result:
                            result.append(quadruplet)
                    hash_table[nums[k]] = k
        return result


        
        
        