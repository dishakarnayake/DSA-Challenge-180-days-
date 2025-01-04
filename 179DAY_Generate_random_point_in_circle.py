import random
import math

class Solution:
    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        while True:
            x = random.uniform(-self.radius, self.radius)
            y = random.uniform(-self.radius, self.radius)
            if x * x + y * y <= self.radius * self.radius:
                return [self.x_center + x, self.y_center + y]



import random
import math

class Solution:
    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        r = math.sqrt(random.uniform(0, 1)) * self.radius
        theta = random.uniform(0, 2 * math.pi)
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        return [x, y]
