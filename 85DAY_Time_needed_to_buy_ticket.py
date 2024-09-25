class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        time = 0
        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    time += 1
                if tickets[k] == 0:
                    return time
        

class Solution:
    def timeRequiredToBuy(self, tickets, k):
        time = 0
        n = len(tickets)
        
        for i in range(n):
            if i <= k:
                time += min(tickets[i], tickets[k])
            else:
                time += min(tickets[i], tickets[k] - 1)
                
        return time


class Solution:
    def timeRequiredToBuy(self, tickets, k):
        time = 0
        
        for i in range(len(tickets)):
            # For people before or at position k, they get to buy up to tickets[k] tickets
            if i <= k:
                time += min(tickets[i], tickets[k])
            # For people after position k, they only get to buy up to tickets[k] - 1 tickets
            else:
                time += min(tickets[i], tickets[k] - 1)
                
        return time
