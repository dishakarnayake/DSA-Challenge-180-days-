# Optimized for Frequent Deletions (Using Length Variable)
# class Solution:
#     def __init__(self):
#         self.length = 0
#     def delete_node(self, head, x):
#         # If the list is empty
#         if not head:
#             return None
        
#         self.length -= 1
        
#         # If the node to be deleted is the head node
#         if x == 1:
#             new_head = head.next
#             if new_head:
#                 new_head.prev = None
#             return new_head
        
#         # Choose to traverse from head or tail based on x
#         if x <= self.length // 2:
#             current = head
#             for i in range(1, x):
#                 current = current.next
#         else:
#             current = head
#             while current.next:
#                 current = current.next
#             for i in range(self.length, x, -1):
#                 current = current.prev
        
#         # Re-link the previous and next nodes
#         if current.next:
#             current.next.prev = current.prev
        
#         if current.prev:
#             current.prev.next = current.next
        
#         return head
       
       
       
# Traverse to the Node and Delete
class Solution:
    def delete_node(self, head, x):
       
        # If the list is empty
        if not head:
            return None
        
        # If the node to be deleted is the head node
        if x == 1:
            new_head = head.next
            if new_head:
                new_head.prev = None
            return new_head
        
        # Traverse the list to find the node at position x
        current = head
        for i in range(1, x):
            current = current.next
        
        # Re-link the previous and next nodes
        if current.next:
            current.next.prev = current.prev
        
        if current.prev:
            current.prev.next = current.next
            
        # Return the head of the list
        return head