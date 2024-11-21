class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(start, target, path):
            if target == 0:
                result.append(list(path))
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()
        
        result = []
        backtrack(0, target, [])
        return result



class Solution:
    def combinationSum(self, candidates, target):
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        
        for c in candidates:
            for t in range(c, target + 1):
                for comb in dp[t - c]:
                    dp[t].append(comb + [c])
        
        return dp[target]





from collections import deque

class Solution:
    def combinationSum(self, candidates, target):
        queue = deque([(0, [], 0)])  # (current_sum, combination, index)
        result = []
        
        while queue:
            curr_sum, comb, start = queue.popleft()
            if curr_sum == target:
                result.append(comb)
                continue
            for i in range(start, len(candidates)):
                if curr_sum + candidates[i] <= target:
                    queue.append((curr_sum + candidates[i], comb + [candidates[i]], i))
        
        return result
