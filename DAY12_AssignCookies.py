
#two pointer approach
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_pointer, s_pointer = 0, 0
        allocations = 0
        while g_pointer < len(g) and s_pointer < len(s):
            if s[s_pointer] >= g[g_pointer]:
                allocations += 1
                s_pointer += 1
                g_pointer += 1
            else:
                s_pointer += 1
        return allocations
    
# brute force method
class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i=0
        j=0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                i+=1
            j+=1
        return i
        