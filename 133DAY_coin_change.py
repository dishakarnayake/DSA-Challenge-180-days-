class Solution:
    def minCoins(self, coins, sum):
        # Memoization dictionary
        memo = {}

        def minCoinsHelper(remaining):
            # Base cases
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')

            # Check if result is already computed
            if remaining in memo:
                return memo[remaining]

            # Recursive case
            min_coins = float('inf')
            for coin in coins:
                result = minCoinsHelper(remaining - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)

            # Store result in memo and return it
            memo[remaining] = min_coins
            return min_coins

        result = minCoinsHelper(sum)
        return -1 if result == float('inf') else result
