
# iterative method
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Solution:
    def getCount(self, head):
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        return count










# Recursive method
class Solution:
    def getCount(self, head):
        # Base case: if the linked list is empty
        if head is None:
            return 0
        # Recursive case: count this node plus the rest of the list
        else:
            return 1 + self.getCount(head.next)





































# using two pointer technique
class Solution:
    def getCount(self, head):
        slow = head
        fast = head
        count = 0
        
        while fast is not None:
            count += 1
            slow = slow.next
            fast = fast.next
            
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        