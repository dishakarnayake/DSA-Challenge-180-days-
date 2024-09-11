
# using  Two  Stacks
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val) :
        self.stack.append(val)
        # Push to min_stack if it is the smallest value seen so far
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) :
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) :
        return self.stack[-1] if self.stack else None

    def getMin(self) :
        return self.min_stack[-1] if self.min_stack else None





# using  single stack with tuples
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val) :
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self) :
        if self.stack:
            self.stack.pop()

    def top(self) :
        return self.stack[-1][0] if self.stack else None

    def getMin(self) :
        return self.stack[-1][1] if self.stack else None
