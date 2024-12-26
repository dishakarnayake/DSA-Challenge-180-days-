import random

class Solution:
    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.m = m
        self.n = n
        self.total = m * n
        self.remaining = self.total
        self.mapping = {}

    def flip(self):
        """
        :rtype: List[int]
        """
        # Pick a random index
        rand_idx = random.randint(0, self.remaining - 1)
        # Find the actual index, considering any remapping
        actual = self.mapping.get(rand_idx, rand_idx)
        # Remap the selected index to the last available index
        self.mapping[rand_idx] = self.mapping.get(self.remaining - 1, self.remaining - 1)
        # Reduce the remaining range
        self.remaining -= 1
        # Convert to 2D coordinates
        return [actual // self.n, actual % self.n]

    def reset(self):
        """
        :rtype: None
        """
        self.remaining = self.total
        self.mapping.clear()


import random

class Solution:
    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.m = m
        self.n = n
        self.total = m * n
        self.indices = list(range(self.total))
        self.remaining = self.total

    def flip(self):
        """
        :rtype: List[int]
        """
        # Pick a random index in the unflipped range
        rand_idx = random.randint(0, self.remaining - 1)
        # Swap the random index with the last unflipped index
        self.indices[rand_idx], self.indices[self.remaining - 1] = self.indices[self.remaining - 1], self.indices[rand_idx]
        # Reduce the remaining range
        self.remaining -= 1
        # Convert to 2D coordinates
        result = self.indices[self.remaining]
        return [result // self.n, result % self.n]

    def reset(self):
        """
        :rtype: None
        """
        self.remaining = self.total
