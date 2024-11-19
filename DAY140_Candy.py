class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n
        
      
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
 
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)


import heapq

class Solution:
    def candy(self, ratings):
        n = len(ratings)
        heap = [(ratings[i], i) for i in range(n)]
        heapq.heapify(heap)
        candies = [1] * n
        
        while heap:
            _, i = heapq.heappop(heap)
            if i > 0 and ratings[i] > ratings[i - 1]:
                candies[i] = max(candies[i], candies[i - 1] + 1)
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)



class Solution:
    def candy(self, ratings):
        n = len(ratings)
        if n == 1:
            return 1
        
        up = down = peak = 0
        candies = 1 
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                up += 1
                peak = up
                down = 0
                candies += 1 + up
            elif ratings[i] < ratings[i - 1]:
                down += 1
                up = 0
                candies += 1 + down - (peak >= down)
            else:
                up = down = peak = 0
                candies += 1
        
        return candies
