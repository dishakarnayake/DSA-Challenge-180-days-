class Solution:
    def partition(self, s):
        def is_palindrome(substring):
            return substring == substring[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start, len(s)):
                if is_palindrome(s[start:end + 1]):
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result





class Solution:
    def partition(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = length == 2 or dp[i + 1][j - 1]
        
        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start, len(s)):
                if dp[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result



class Solution:
    def partition(self, s):
        result = []
        stack = [(0, [])]

        def is_palindrome(substring):
            return substring == substring[::-1]

        while stack:
            start, path = stack.pop()
            if start == len(s):
                result.append(path)
                continue
            for end in range(start, len(s)):
                if is_palindrome(s[start:end + 1]):
                    stack.append((end + 1, path + [s[start:end + 1]]))
        
        return result
