class Solution:
    def AllPossibleStrings(self, s):
        n = len(s)
        result = []
        for mask in range(1, 1 << n):  # Iterate from 1 to 2^n - 1
            subseq = ""
            for i in range(n):
                if mask & (1 << i):  # Check if the i-th bit is set
                    subseq += s[i]
            result.append(subseq)
        result.sort()  # Sort lexicographically
        return result




class Solution:
    def AllPossibleStrings(self, s):
        def backtrack(index, current):
            if index == len(s):
                if current:  # Add non-empty subsequences
                    result.append(current)
                return
            
            # Exclude current character
            backtrack(index + 1, current)
            # Include current character
            backtrack(index + 1, current + s[index])
        
        result = []
        backtrack(0, "")
        result.sort()  # Sort lexicographically
        return result






class Solution:
    def AllPossibleStrings(self, s):
        result = [""]
        for char in s:
            result += [subseq + char for subseq in result]
        
        result = [seq for seq in result if seq]  # Remove the empty string
        result.sort()  # Sort lexicographically
        return result
