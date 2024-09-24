from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()  

    def ping(self, t):
        self.requests.append(t)
        
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        
        return len(self.requests)

        
class RecentCounter:
    def __init__(self):
        self.requests = [] 

    def ping(self, t):
        self.requests.append(t)
        count = 0
        for time in self.requests:
            if time >= t - 3000:
                count += 1
                
        return count



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)