
'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
'''
#iterative method
class Solution:
    def reverseDLL(self, head):
        #return head after reversing
        if not head:  # Empty list
            return None
        
        current = head
        while current:
            # Swap next and prev pointers
            current.prev, current.next = current.next, current.prev
            
            # Move to the next node in the original order
            head = current  # Update head to the current node
            current = current.prev  # Move to the next node (which is now previous)
        
        return head

#recursive approach

class Solution:
    def reverseDLL(self, head):
        if not head:
            return None

        # Base case: If this is the last node, it will be the new head
        if not head.next:
            head.prev, head.next = head.next, head.prev
            return head

        # Recursively reverse the rest of the list
        new_head = self.reverseDLL(head.next)

        # Adjust pointers
        head.next.next = head
        head.prev = head.next
        head.next = None

        return new_head
        
# using stack
class Solution:
    def reverseDLL(self, head):
        if not head:
            return None
        
        stack = []
        current = head
        
        # Push all nodes onto the stack
        while current:
            stack.append(current)
            current = current.next
        
        # Pop nodes and adjust pointers
        new_head = stack.pop()
        current = new_head
        while stack:
            node = stack.pop()
            current.next = node
            node.prev = current
            current = node
        
        current.next = None  # Last node's next should be None
        return new_head