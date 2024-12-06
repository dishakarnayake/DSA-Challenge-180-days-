class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        word_set = set(words)
        result = []

        def canForm(word):
            dp = [False] * (len(word) + 1)
            dp[0] = True  
            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set and word[j:i] != word:
                        dp[i] = True
                        break
            return dp[len(word)]

        for word in words:
            if canForm(word):
                result.append(word)
        return result


class Solution:
    def findAllConcatenatedWordsInADict(self,words):
        word_set = set(words)
        memo = {}

        def canForm(word):
            if word in memo:
                return memo[word]
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set and (suffix in word_set or canForm(suffix)):
                    memo[word] = True
                    return True
            memo[word] = False
            return False

        result = []
        for word in words:
            if canForm(word):
                result.append(word)
        return result