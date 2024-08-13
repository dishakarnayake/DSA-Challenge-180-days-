class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def insertAtEnd(self, head, x):
        # Create a new node with the value x
        new_node = Node(x)
        
        # If the list is empty, return the new node as the head
        if head is None:
            return new_node
        
        # Traverse to the end of the linked list
        current = head
        while current.next:
            current = current.next
        
        # Set the next of the last node to the new node
        current.next = new_node
        
        # Return the head of the linked list
        return head


class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class solution:
    def insertAtEnd(self, head, tail, x):
        # Create a new node with the value x
        new_node = Node(x)
        
        # If the list is empty, return the new node as both head and tail
        if head is None:
            return new_node, new_node
        
        # Use the tail pointer to add the new node at the end
        tail.next = new_node
        tail = new_node
        
        # Return the head and updated tail of the linked list
        return head, tail