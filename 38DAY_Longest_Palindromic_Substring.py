#Brute Force Method
class Solution(object):
    def longestPalindrome(self, s):
        def is_palindrome(s):
            return s == s[::-1]
        n = len(s)
        if n == 0:
            return ""
        max_length = 1
        start = 0
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if is_palindrome(substring) and len(substring) > max_length:
                    max_length = len(substring)
                    start = i
        return s[start:start + max_length]



# Dynamic Programming
class Solution(object):
    def longestPalindrome(self, s):

        n = len(s)
        if n == 0:
            return ""
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_length = 1

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_length = 2

        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start = i
                    max_length = length

        return s[start:start + max_length]


# Expand Around Center Approach
class Solution(object):
    def longestPalindrome(self, s):
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        if len(s) == 0:
            return ""
        max_palindrome = ""
        for i in range(len(s)):
            # Odd length palindrome
            palindrome1 = expand_around_center(s, i, i)
            # Even length palindrome
            palindrome2 = expand_around_center(s, i, i + 1)
            # Update max_palindrome if a longer one is found
            max_palindrome = max(max_palindrome, palindrome1, palindrome2, key=len)
        return max_palindrome