class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, val, wt, capacity):
        #code here
        items = [(val[i], wt[i]) for i in range(len(val))]
        
        # Sort items by value-to-weight ratio in descending order
        items.sort(key=lambda x: x[0] / x[1], reverse=True)
        
        max_value = 0.0  # Total maximum value
        for value, weight in items:
            if capacity == 0:
                break  # Knapsack is full
            if weight <= capacity:
                # Take the whole item
                max_value += value
                capacity -= weight
            else:
                # Take a fraction of the item
                max_value += (value / weight) * capacity
                capacity = 0
        
        # Return the max value rounded to 6 decimal places
        return round(max_value, 6)