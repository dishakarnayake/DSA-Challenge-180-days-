

#Brute force method
class Solution(object):
    def maxProfit(self, prices):
       
            max_profit = 0
            for i in range(len(prices)):
                for j in range(i + 1, len(prices)):
                    profit = prices[j] - prices[i]
                    if profit > max_profit:
                        max_profit = profit
            return max_profit
        
        
#using  one pass
class solution(object):
    def maxProfit( self,prices):
           
            if not prices:
                return 0
            min_price = prices[0]
            max_profit = 0
            for price in prices:
                if price < min_price:
                    min_price = price
                else:
                    max_profit = max(max_profit, price - min_price)
            return max_profit
        
#using  Dynamic programming
class So_lution(object):
    def maxProfit( self,prices):
 
        if not prices:
            return 0
        dp = [0] * len(prices)
        min_price = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return dp[-1]