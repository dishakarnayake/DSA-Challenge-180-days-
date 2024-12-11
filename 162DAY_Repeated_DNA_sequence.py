class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []
        
        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            substring = s[i:i + 10]
            if substring in seen:
                repeated.add(substring)
            else:
                seen.add(substring)

        return list(repeated)


class solution:
    def findRepeatedDnaSequences_approach2(self, s):
        if len(s) < 10:
            return []

        char_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        hash_val = 0
        seen = set()
        repeated = set()

        for i in range(len(s)):
            # Add current character to hash
            hash_val = (hash_val << 2) | char_map[s[i]]
            # Only consider sequences of length 10
            if i >= 9:
                # Keep hash value within 20 bits
                hash_val &= (1 << 20) - 1
                if hash_val in seen:
                    repeated.add(s[i - 9:i + 1])
                else:
                    seen.add(hash_val)

        return list(repeated)
        