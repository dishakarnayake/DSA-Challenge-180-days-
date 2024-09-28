class MyCircularQueue:

    def __init__(self, k):
        self.queue = [0] * k  # Fixed size array to store elements
        self.max_size = k     # Maximum size of the circular queue
        self.front = 0        # Pointer to the front of the queue
        self.rear = -1        # Pointer to the rear of the queue
        self.size = 0         # Current number of elements in the queue

    def enQueue(self, value):
        if self.isFull():      # Check if the queue is full
            return False
        self.rear = (self.rear + 1) % self.max_size  # Circular increment
        self.queue[self.rear] = value
        self.size += 1         # Increment the size
        return True

    def deQueue(self) :
        if self.isEmpty():     # Check if the queue is empty
            return False
        self.front = (self.front + 1) % self.max_size  # Circular increment
        self.size -= 1         # Decrement the size
        return True

    def Front(self) :
        if self.isEmpty():     # If the queue is empty, return -1
            return -1
        return self.queue[self.front]  # Return the front element

    def Rear(self) :
        if self.isEmpty():     # If the queue is empty, return -1
            return -1
        return self.queue[self.rear]  # Return the rear element

    def isEmpty(self) :
        return self.size == 0  # Queue is empty if size is 0

    def isFull(self):
        return self.size == self.max_size  # Queue is full if size equals max_size




class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyCircularQueue:
    def __init__(self, k):
        self.max_size = k
        self.size = 0
        self.front = None
        self.rear = None

    def enQueue(self, value) :
        if self.isFull():
            return False
        new_node = Node(value)
        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
            self.rear.next = self.front  # Circular link
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front  # Maintain circular property
        self.size += 1
        return True

    def deQueue(self) :
        if self.isEmpty():
            return False
        if self.front == self.rear:  # Only one element in the queue
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front  # Maintain circular property
        self.size -= 1
        return True

    def Front(self) :
        if self.isEmpty():
            return -1
        return self.front.value

    def Rear(self) :
        if self.isEmpty():
            return -1
        return self.rear.value

    def isEmpty(self) :
        return self.size == 0

    def isFull(self) :
        return self.size == self.max_size
