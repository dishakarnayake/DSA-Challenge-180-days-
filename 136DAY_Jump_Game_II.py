class Solution:
    def jump(self, nums):
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):  # No need to jump from the last index
            farthest = max(farthest, i + nums[i])
            if i == current_end:  # Time to make a jump
                jumps += 1
                current_end = farthest
                
        return jumps



class Solution:
    def jump(self, nums):
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0  # Start with 0 jumps at the first index

        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

        return dp[-1]



class Solution:
    def jump(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        
        level = 0
        current_max = 0
        next_max = 0
        i = 0

        while i <= current_max:
            level += 1
            while i <= current_max:
                next_max = max(next_max, i + nums[i])
                if next_max >= n - 1:
                    return level
                i += 1
            current_max = next_max

        return -1
