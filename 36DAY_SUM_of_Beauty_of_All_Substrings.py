#Approach 1: Brute Force

class Solution(object):
    def beautySum(self, s):
        def beauty(sub):
            freq = [0] * 26
            for char in sub:
                freq[ord(char) - ord('a')] += 1
            max_freq = max(freq)
            min_freq = min([f for f in freq if f > 0])
            return max_freq - min_freq

        n = len(s)
        total_beauty = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                total_beauty += beauty(s[i:j])
        return total_beauty








# Approach 2: Optimized Brute Force with Frequency Array

class Solution(object):
    def beautySum(self, s):
        n = len(s)
        total_beauty = 0

        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                max_freq = max(freq)
                min_freq = min([f for f in freq if f > 0])
                total_beauty += max_freq - min_freq

        return total_beauty



# Approach 3: Sliding Window with Dynamic Frequency Count
class Solution(object):
    def beautySum(self, s):
        n = len(s)
        total_beauty = 0

        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                max_freq = max(freq)
                min_freq = min([f for f in freq if f > 0])
                total_beauty += max_freq - min_freq

        return total_beauty
