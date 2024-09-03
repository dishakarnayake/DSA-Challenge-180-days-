
'''
# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
		        self.prev = None
'''
# Iterative Approach
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        if not head:
            return None
        
        current = head
        
        while current and current.next:
            if current.data == current.next.data:
                # Remove the duplicate node
                next_node = current.next
                current.next = next_node.next
                if next_node.next:
                    next_node.next.prev = current
            else:
                current = current.next
        
        return head
        
        
        
# Recursive Approach
class Solution:
    # Function to remove duplicates from a sorted doubly linked list using recursion.
    def removeDuplicates(self, head):
        if not head or not head.next:
            return head
        
        # Recursive call for the rest of the list
        head.next = self.removeDuplicates(head.next)
        
        # If the next node is a duplicate, skip it
        if head.data == head.next.data:
            next_node = head.next
            head.next = next_node.next
            if head.next:
                head.next.prev = head
        
        return head