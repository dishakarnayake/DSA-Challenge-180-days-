class Solution:
    def mostPoints(self, questions):
        
        n = len(questions)
        
        memo = [-1] * n
        
        def dp(index):
            if index >= n:
                return 0
            
            if memo[index] != -1:
                return memo[index]
            
            solve = questions[index][0] + dp(index + questions[index][1] + 1)
            
            skip = dp(index + 1)
            memo[index] = max(solve, skip)
            
            return memo[index]
        
        return dp(0)







class Solution:
    def mostPoints(self, questions):
        n = len(questions)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            solve = questions[i][0]
            next_question = i + questions[i][1] + 1
            if next_question < n:
                solve += dp[next_question]
            
            skip = dp[i + 1]
            
            dp[i] = max(solve, skip)
        
        return dp[0]



