class Solution:
    def combinationSum2(self, candidates, target):
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()

        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result


class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        stack = [(0, target, [])]

        while stack:
            index, remaining, path = stack.pop()
            if remaining == 0:
                result.append(path)
                continue

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                stack.append((i + 1, remaining - candidates[i], path + [candidates[i]]))

        return result


class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        dp = [set() for _ in range(target + 1)]
        dp[0].add(())

        for num in candidates:
            for t in range(target, num - 1, -1):
                for comb in dp[t - num]:
                    dp[t].add(tuple(sorted(comb + (num,))))

        return [list(comb) for comb in dp[target]]

        