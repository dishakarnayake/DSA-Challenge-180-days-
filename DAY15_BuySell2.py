class Solution(object):
    def maxProfit(self, prices):


      
# brute force approach      
        pr=0
        for i in range(1, len(prices)):
            if(prices[i] > prices[i-1]):
                pr =  pr + (prices[i]-prices[i-1])

        return pr         #time complexity O(n^2) space complexity O(1)



# peak valley approach    
        max_profit = 0
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley
        return max_profit  #time complexity O(n) space complexity O(1)

# One pass Approach
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit    #time complexity O(n) space complexity O(1)