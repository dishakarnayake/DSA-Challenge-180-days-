class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        always_satisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                always_satisfied += customers[i]
        
        # Step 2: Sliding window to calculate the maximum extra satisfaction
        max_extra_satisfied = 0
        current_extra_satisfied = 0
        
        for i in range(len(customers)):
            # Add the current minute's extra customers if grumpy
            if grumpy[i] == 1:
                current_extra_satisfied += customers[i]
            
            # Slide the window: remove the leftmost element if window exceeds size
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    current_extra_satisfied -= customers[i - minutes]
            
            # Update the maximum extra satisfied customers
            max_extra_satisfied = max(max_extra_satisfied, current_extra_satisfied)
        
        # Step 3: Total satisfied customers
        return always_satisfied + max_extra_satisfied
        


class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        n = len(customers)
        
        # Calculate prefix sum of customers
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + customers[i]
        
        # Calculate the always satisfied customers
        always_satisfied = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        
        # Find the maximum additional customers by using the secret technique
        max_extra_satisfied = 0
        for i in range(n - minutes + 1):
            # Gain from the secret technique
            extra_satisfied = prefix[i + minutes] - prefix[i]
            # Subtract already satisfied customers in this range
            for j in range(i, i + minutes):
                if grumpy[j] == 0:
                    extra_satisfied -= customers[j]
            max_extra_satisfied = max(max_extra_satisfied, extra_satisfied)
        
        return always_satisfied + max_extra_satisfied
