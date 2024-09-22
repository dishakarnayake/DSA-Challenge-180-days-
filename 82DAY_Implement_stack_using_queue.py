from collections import deque
# using two queues (Push operation)
class MyStack:
    def __init__(self):
        self.queue1 = deque()  # Main queue
        self.queue2 = deque()  # Helper queue

    def push(self, x) :
        # Push to the empty queue2
        self.queue2.append(x)
        
        # Move all elements from queue1 to queue2 to reverse the order
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        
        # Swap the names of the two queues
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        # Remove the front of queue1
        return self.queue1.popleft()

    def top(self):
        # Peek the front of queue1
        return self.queue1[0]

    def empty(self):
        return not self.queue1



# using one Queue (Pop Operation)
from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()  # Use a single queue

    def push(self, x) :
        self.queue.append(x)
        # Rotate the queue so that the new element is at the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        # Remove the front of the queue (top of stack)
        return self.queue.popleft()

    def top(self) :
        # Peek the front of the queue (top of stack)
        return self.queue[0]

    def empty(self) :
        return not self.queue
