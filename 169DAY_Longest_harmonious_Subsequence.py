class Solution(object):
    def findLHS(self, nums):
        freq = Counter(nums)
        max_length = 0
        for key in freq:
            if key + 1 in freq:
                max_length = max(max_length, freq[key] + freq[key + 1])
        return max_length
        
class Solution(object):
    def findLHS(self,nums):
        nums.sort()
        i = 0
        max_length = 0
        for j in range(len(nums)):
            while nums[j] - nums[i] > 1:
                i += 1
            if nums[j] - nums[i] == 1:
                max_length = max(max_length, j - i + 1)
        return max_length
