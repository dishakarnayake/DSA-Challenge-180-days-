# stack approach
class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack
        


# regular expresson
import re

class Solution:
    def isValid(self, s):
        while re.search(r'\(\)|\{}|\[]', s):
            s = re.sub(r'\(\)|\{}|\[]', '', s)
        return s == ''




# recursive approach
class Solution:
    def isValid(self, s) :
        def remove_pairs(s):
            if '()' in s:
                return remove_pairs(s.replace('()', ''))
            if '{}' in s:
                return remove_pairs(s.replace('{}', ''))
            if '[]' in s:
                return remove_pairs(s.replace('[]', ''))
            return s

        return remove_pairs(s) == ''








