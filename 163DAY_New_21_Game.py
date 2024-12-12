class Solution(object):
    def new21Game(self, n, k, maxPts):
        if k == 0 or n >= k + maxPts:
            return 1.0
        
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        
        window_sum = 1.0
        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            if i < k:
                window_sum += dp[i]
            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]
        
        return sum(dp[k:])


import random

class Solution:
    def new21Game(self, n, k, maxPts):
        num_simulations = 100000
        success_count = 0

        for _ in range(num_simulations):
            score = 0
            while score < k:
                score += random.randint(1, maxPts)
            if score <= n:
                success_count += 1

        return success_count / num_simulations



class Solution:
    def new21Game(self, n, k, maxPts):
        if k == 0 or n >= k + maxPts:
            return 1.0
        
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        prefix_sum = 1.0
        result = 0.0
        
        for i in range(1, n + 1):
            dp[i] = prefix_sum / maxPts
            if i < k:
                prefix_sum += dp[i]
            else:
                result += dp[i]
            if i - maxPts >= 0:
                prefix_sum -= dp[i - maxPts]
        
        return result
