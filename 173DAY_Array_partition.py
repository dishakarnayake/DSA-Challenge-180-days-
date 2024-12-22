class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2])
        

class Solution:
    def arrayPairSum(self, nums):
        min_val, max_val = min(nums), max(nums)
        offset = -min_val
        freq = [0] * (max_val - min_val + 1)
        
        for num in nums:
            freq[num + offset] += 1
        
        sum_result, pick = 0, True
        for i in range(len(freq)):
            while freq[i] > 0:
                if pick:
                    sum_result += i - offset
                pick = not pick
                freq[i] -= 1
        
        return sum_result