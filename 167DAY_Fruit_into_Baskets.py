class Solution(object):
    def totalFruit(self, fruits):
        max_fruits = 0
        basket = {}
        left = 0

        for right in range(len(fruits)):
            # Add current fruit to the basket
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1
            
            # If there are more than 2 types of fruits, shrink the window
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            
            # Update the maximum fruits picked
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits




class Solution:
    def totalFruit(self, fruits):
        from collections import defaultdict

        fruit_count = defaultdict(int)
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            fruit_count[fruits[right]] += 1
            
            # Check if the basket contains more than two types of fruits
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits

