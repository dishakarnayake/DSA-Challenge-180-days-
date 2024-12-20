class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        
        def counting_sort(exp):
            n = len(nums)
            output = [0] * n
            count = [0] * 10
            
            for num in nums:
                index = (num // exp) % 10
                count[index] += 1
            
            for i in range(1, 10):
                count[i] += count[i - 1]
            
            for i in range(n - 1, -1, -1):
                index = (nums[i] // exp) % 10
                output[count[index] - 1] = nums[i]
                count[index] -= 1
            
            for i in range(n):
                nums[i] = output[i]
        
        max_num = max(nums)
        exp = 1
        while max_num // exp > 0:
            counting_sort(exp)
            exp *= 10
        
        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i] - nums[i - 1])
        
        return max_gap
        