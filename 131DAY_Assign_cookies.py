class Solution(object):
    def findContentChildren(self, g, s):
        # Sort greed factors and cookie sizes
        g.sort()
        s.sort()
        
        child = 0  # Pointer for g (children)
        cookie = 0  # Pointer for s (cookies)
        
        # Iterate until we run out of children or cookies
        while child < len(g) and cookie < len(s):
            # If the cookie can satisfy the child, assign it
            if s[cookie] >= g[child]:
                child += 1  # Move to the next child
            # Move to the next cookie regardless of satisfaction
            cookie += 1
        
        return child






import heapq

class Solution:
    def findContentChildren(self, g, s):
        # Convert greed and cookie lists into max-heaps by using negative values
        g = [-i for i in g]
        s = [-i for i in s]
        
        # Heapify the lists
        heapq.heapify(g)
        heapq.heapify(s)
        
        content_children = 0
        
        # Continue while there are both children and cookies
        while g and s:
            # Check if the largest cookie can satisfy the largest unsatisfied child
            if -s[0] >= -g[0]:  # Compare absolute values
                # Cookie satisfies child, pop both
                heapq.heappop(g)
                heapq.heappop(s)
                content_children += 1
            else:
                # If the cookie is too small, discard it
                heapq.heappop(s)
        
        return content_children
