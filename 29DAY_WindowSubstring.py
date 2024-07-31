#Python collections
from collections import Counter
class Solution(object):
        def minWindow(self,s, t):
            t_count = Counter(t)
            required = len(t_count)
            l, r = 0, 0
            formed = 0
            window_counts = Counter()
            ans = float("inf"), None, None

            while r < len(s):
                character = s[r]
                window_counts[character] += 1
                if character in t_count and window_counts[character] == t_count[character]:
                    formed += 1

                while l <= r and formed == required:
                    character = s[l]
                    if r - l + 1 < ans[0]:
                        ans = (r - l + 1, l, r)
                    window_counts[character] -= 1
                    if character in t_count and window_counts[character] < t_count[character]:
                        formed -= 1
                    l += 1    
                r += 1    
            return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]







    # sliding window
        # def minWindow(self,s, t):
            # t_count = {}
            # for char in t:
            #     t_count[char] = t_count.get(char, 0) + 1
            # required = len(t_count)
            # l, r = 0, 0
            # formed = 0
            # window_counts = {}
            # ans = float("inf"), None, None

            # while r < len(s):
            #     character = s[r]
            #     window_counts[character] = window_counts.get(character, 0) + 1
            #     if character in t_count and window_counts[character] == t_count[character]:
            #         formed += 1

            #     while l <= r and formed == required:
            #         character = s[l]
            #         if r - l + 1 < ans[0]:
            #             ans = (r - l + 1, l, r)
            #         window_counts[character] -= 1
            #         if character in t_count and window_counts[character] < t_count[character]:
            #             formed -= 1
            #         l += 1    
            #     r += 1    
            # return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]





    # Brute force approach
        # def minWindow(self,s, t):
        #     def check(window):
        #         t_count = {}
        #         for char in t:
        #             t_count[char] = t_count.get(char, 0) + 1
        #         for char in window:
        #             if char in t_count:
        #                 t_count[char] -= 1
        #                 if t_count[char] == 0:
        #                     del t_count[char]
        #         return len(t_count) == 0

        #     min_window = ""
        #     for i in range(len(s)):
        #         for j in range(i + 1, len(s) + 1):
        #             window = s[i:j]
        #             if check(window):
        #                 if not min_window or len(window) < len(min_window):
        #                     min_window = window
        #     return min_window

















    # def minWindow(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: str
    #     """
    #     letterDict = {}

    #     if t in s:
    #         return t

    #     for letter in t:
    #         if letter in letterDict:
    #             letterDict[letter] += 1
    #         else:
    #             letterDict[letter] = 1

    #     currWindow, currLen = [], 0
    #     minLen, n = float("inf"), len(s)
    #     left = 0
    #     currLetterDict = {}
    #     required = len(letterDict)
    #     retLeft, retRight = 0, 0
    #     count = 0

    #     for right in range(n):
    #         letter = s[right]

    #         if letter in letterDict:
    #             if letter in currLetterDict:
    #                 currLetterDict[letter] += 1
    #             else:
    #                 currLetterDict[letter] = 1

    #             if currLetterDict[letter] == letterDict[letter]:
    #                 count += 1

    #         while count == required:
    #             # valid substring
    #             currLen = right - left + 1
    #             # update res
    #             if currLen < minLen:
    #                 minLen = currLen
    #                 retLeft, retRight = left, right
                
    #             # update new curr letter letterDict
    #             if s[left] in currLetterDict:
    #                 currLetterDict[s[left]] -= 1
    #                 if currLetterDict[s[left]] < letterDict[s[left]]:
    #                     count -= 1
    #             left += 1

    #     return s[retLeft:retRight+1] if minLen != float("inf") else ""