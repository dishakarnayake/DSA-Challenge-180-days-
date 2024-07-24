# Find THe Index Of First Occurence in the String
# Brute Force Approach
class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
obj = Solution()
haystack = "hello"
needle = "ll"
print(obj.strStr(haystack, needle))
# time complexity O(n)
# space complexity O(1)






# Two pointer approach
class solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)

        # Preprocessing
        pre = 0
        for i in range(1, len(needle)):
            while pre > 0 and needle[i] != needle[pre]:
                pre = lps[pre-1]
            if needle[pre] == needle[i]:
                pre += 1
                lps[i] = pre

        # Main algorithm
        n = 0 #needle index
        for h in range(len(haystack)):
            while n > 0 and needle[n] != haystack[h]:
                n = lps[n-1]
            if needle[n] == haystack[h]:
                n += 1
            if n == len(needle):
                return h - n + 1

        return -1
obj = solution()
haystack = "sadbutsad"
needle = "sad"
print(obj.strStr(haystack, needle))
# time complexity O(n)
# space complexity O(n)