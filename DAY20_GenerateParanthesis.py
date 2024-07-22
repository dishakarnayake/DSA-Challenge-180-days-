class Solution:
    # Backtracking
    def generateParenthesis(self, n) :
            def backtrack(s, left, right):
                if len(s) == 2 * n:
                    result.append(s)
                    return
                if left < n:
                    backtrack(s + "(", left + 1, right)
                if right < left:
                    backtrack(s + ")", left, right + 1)

            result = []
            backtrack("", 0, 0)
            return result




    #Using Dynamic programming
        # dp = [[] for _ in range(n + 1)]
        # dp[0].append("")
        # for i in range(n + 1):
        #     for j in range(i):
        #         for s1 in dp[j]:
        #             for s2 in dp[i - 1 - j]:
        #                 dp[i].append("(" + s1 + ")" + s2)
        # return dp[n]









        #Using recursion funtion


        # def generate(p, left, right, parens=[]):
        #         if left:         generate(p + '(', left-1, right)
        #         if right > left: generate(p + ')', left, right-1)
        #         if not right:    parens += p,
        #         return parens
        # return generate('', n, n)










# usinf iterative method
        # result = []
        # queue = [("", 0, 0)]
        # while queue:
        #     s, left, right = queue.pop(0)
        #     if left == n and right == n:
        #         result.append(s)
        #     if left < n:
        #         queue.append((s + "(", left + 1, right))
        #     if right < left:
        #         queue.append((s + ")", left, right + 1))
        # return result






        # res = []

        # def dfs(openP, closeP, s):
        #     if openP == closeP and openP + closeP == n * 2:
        #         res.append(s)
        #         return
            
        #     if openP < n:
        #         dfs(openP + 1, closeP, s + "(")
            
        #     if closeP < openP:
        #         dfs(openP, closeP + 1, s + ")")

        # dfs(0, 0, "")

        # return res