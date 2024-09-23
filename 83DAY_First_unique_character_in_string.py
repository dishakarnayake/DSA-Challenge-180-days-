# using hashmap
class Solution(object):
    def firstUniqChar(self, s):
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        
        return -1



# using list for counting
class Solution(object):
    def firstUniqChar(self, s):
        char_count = [0] * 26
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        
        for index, char in enumerate(s):
            if char_count[ord(char) - ord('a')] == 1:
                return index
        
        return -1


# using two passes with set
class Solution(object):
    def firstUniqChar(self, s):
        seen = set()
        unique = {}
        
        for index, char in enumerate(s):
            if char in unique:
                seen.add(char)
                del unique[char]
            elif char not in seen:
                unique[char] = index
    
        if unique:
            return min(unique.values())
        
        return -1