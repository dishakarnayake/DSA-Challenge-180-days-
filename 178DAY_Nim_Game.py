class Solution(object):
    def canWinNim(self, n):
        return n % 4 != 0


class Solution(object):
    def __init__(self):
        self.memo = {}
    
    def canWinNim(self, n):
        if n in self.memo:
            return self.memo[n]
        
        if n <= 3:
            return True
        
        for i in range(1, 4):
            if not self.canWinNim(n - i):
                self.memo[n] = True
                return True
        
        self.memo[n] = False
        return False

