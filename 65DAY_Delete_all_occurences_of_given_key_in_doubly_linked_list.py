'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
# iterative method
class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        # code here
        # edit the linked list
        # Start with the head node
        current = head
        
        # Traverse the list
        while current:
            if current.data == x:
                # Update the next pointer of the previous node if it exists
                if current.prev:
                    current.prev.next = current.next
                else:
                    # If current is head, move the head pointer
                    head = current.next
                
                # Update the prev pointer of the next node if it exists
                if current.next:
                    current.next.prev = current.prev
                
            # Move to the next node
            current = current.next
        
        # Return the modified list
        return head
        
        
        
        
        
        
        
        
        #  recursive method
        class Solution:
    def deleteAllOccurOfX(self, head, x):
        # Base case: If the list is empty
        if not head:
            return None
        
        # Recur for the rest of the list
        head.next = self.deleteAllOccurOfX(head.next, x)
        
        # If the next node exists, update its previous pointer
        if head.next:
            head.next.prev = head
        
        # If the current node contains the key, delete it
        if head.data == x:
            next_node = head.next
            # Update the previous pointer of the next node
            if next_node:
                next_node.prev = head.prev
            return next_node
        
        return head