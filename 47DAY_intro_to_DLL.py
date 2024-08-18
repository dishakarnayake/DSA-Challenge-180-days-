
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def constructDLL(self, arr):
        if not arr:
            return None
        
        # Create the head of the DLL
        head = Node(arr[0])
        current = head
        
        # Iterate over the rest of the array and create the DLL
        for i in range(1, len(arr)):
            new_node = Node(arr[i])
            current.next = new_node  # Link the current node to the new node
            new_node.prev = current  # Link the new node back to the current node
            current = new_node  # Move to the next node
        
        return head