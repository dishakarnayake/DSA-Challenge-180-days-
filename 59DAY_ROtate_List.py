# Modular Calculation
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length and connect the tail to the head
        length = 1
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
        old_tail.next = head  # Connect tail to head
        
        # Step 2: Find the new tail and new head
        k = k % length
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # Step 3: Break the ring
        new_tail.next = None
        
        return new_head



# Brute Force 
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        length = 0
        curr = head
        
        # Calculate the length of the linked list
        while curr:
            length += 1
            curr = curr.next
        
        k = k % length  # Normalize k
        if k == 0:
            return head
        
        for _ in range(k):
            prev = None
            curr = head
            while curr.next:
                prev = curr
                curr = curr.next
            # Move last node to the front
            curr.next = head
            prev.next = None
            head = curr
        
        return head



# using  Deque
from collections import deque

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        dq = deque()
        curr = head
        while curr:
            dq.append(curr)
            curr = curr.next
        
        k = k % len(dq)  # Normalize k
        if k == 0:
            return head
        
        dq.rotate(k)  # Rotate the deque by k
        
        # Rebuild the linked list
        new_head = dq[0]
        curr = new_head
        for node in list(dq)[1:]:
            curr.next = node
            curr = curr.next
        curr.next = None
        
        return new_head
