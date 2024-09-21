#Lazy transfer
class MyQueue:

    def __init__(self):
        self.stack1 = []  # Stack for pushing elements
        self.stack2 = []  # Stack for popping elements

    def push(self, x) :
        self.stack1.append(x)

    def pop(self) :
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) :
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) :
        return not self.stack1 and not self.stack2





# Eager push
class MyQueue:

    def __init__(self):
        self.stack1 = []  # Stack for holding elements

    def push(self, x):
        temp_stack = []
        while self.stack1:
            temp_stack.append(self.stack1.pop())
        self.stack1.append(x)
        while temp_stack:
            self.stack1.append(temp_stack.pop())

    def pop(self):
        return self.stack1.pop()

    def peek(self) :
        return self.stack1[-1]

    def empty(self) :
        return not self.stack1
