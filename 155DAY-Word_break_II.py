class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = [""]  # Base case: empty string
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wordSet:
                    for sentence in dp[j]:
                        dp[i].append((sentence + " " + s[j:i]).strip())
        
        return dp[len(s)]
        

class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}

        def dfs(index):
            if index in memo:
                return memo[index]
            if index == len(s):
                return [""]
            
            sentences = []
            for end in range(index + 1, len(s) + 1):
                word = s[index:end]
                if word in wordSet:
                    for sub in dfs(end):
                        sentences.append((word + " " + sub).strip())
            memo[index] = sentences
            return sentences

        return dfs(0)


