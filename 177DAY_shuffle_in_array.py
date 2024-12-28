import random

class Solution:
    def __init__(self, nums):
        
        self.original = nums[:]
        self.array = nums[:]

    def reset(self):
        
        self.array = self.original[:]
        return self.array

    def shuffle(self):
        
        for i in range(len(self.array) - 1, 0, -1):
            j = random.randint(0, i)  # Pick a random index
            self.array[i], self.array[j] = self.array[j], self.array[i]  # Swap
        return self.array



import random

class Solution:
    def __init__(self, nums):
        
        self.original = nums[:]
        self.array = nums[:]

    def reset(self):
        
        self.array = self.original[:]
        return self.array

    def shuffle(self):
        
        shuffled = self.array[:]
        random.shuffle(shuffled)
        return shuffled