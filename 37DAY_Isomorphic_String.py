# using character position
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.transform(s) == self.transform(t)
    
    def transform(self, string):
        mapping = {}
        transformed = []
        next_char = 0

        for char in string:
            if char not in mapping:
                mapping[char] = next_char
                next_char += 1
            transformed.append(mapping[char])

        return transformed





# Using a Single dictionary and set
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        mapping = {}
        mapped = set()

        for char_s, char_t in zip(s, t):
            if char_s in mapping:
                if mapping[char_s] != char_t:
                    return False
            else:
                if char_t in mapped:
                    return False
                mapping[char_s] = char_t
                mapped.add(char_t)

        return True


# Using Two Dictionary 
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True
