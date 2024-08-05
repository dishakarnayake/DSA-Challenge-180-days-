
# concatenate and check
class Solution(object):
    def rotateString(self, s, goal):
        return goal in s + s
# time complexity O(n^2)
# space complexity O(n)




#Brute force approach
class Solution(object):
    def rotateString(self, s, goal):
    #     for i in range(len(s)):
    #     # Shift s by i positions
    #     shifted_s = s[i:] + s[:i]
    #     if shifted_s == goal:
    #         return True
    # return False
# time complexity O(n^2)
# space complexity O(n)










