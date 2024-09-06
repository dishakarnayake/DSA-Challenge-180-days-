
'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
# recursive  merge two list
class Solution:
    # Function to merge two sorted linked lists
    def mergeTwoLists(self, a, b):
        # If one of the lists is empty, return the other list
        if a is None:
            return b
        if b is None:
            return a

        # Compare the data and link nodes accordingly
        if a.data < b.data:
            result = a
            result.bottom = self.mergeTwoLists(a.bottom, b)
        else:
            result = b
            result.bottom = self.mergeTwoLists(a, b.bottom)
        
        result.next = None  # We only care about the bottom pointer
        return result

    # Function to flatten the list
    def flatten(self, root):
        #Your code here
        # Base case
        if root is None or root.next is None:
            return root
        
        # Flatten the next part of the list
        root.next = self.flatten(root.next)
        
        # Merge current root and the flattened list
        root = self.mergeTwoLists(root, root.next)

        return root
        
        
# using min heap
import heapq

class Solution:
    def flatten(self, root):
        # Base case
        if not root:
            return None
        
        # Min-heap to store nodes based on their data
        heap = []
        
        # Insert all heads of the sub-lists into the heap
        temp = root
        while temp:
            heapq.heappush(heap, (temp.data, temp))
            temp = temp.next
        
        # Dummy node to start the flattened list
        dummy = Node(0)
        current = dummy
        
        # While heap is not empty
        while heap:
            val, node = heapq.heappop(heap)
            # Add the minimum node to the result list
            current.bottom = node
            current = current.bottom
            
            # If there's a bottom node, add it to the heap
            if node.bottom:
                heapq.heappush(heap, (node.bottom.data, node.bottom))
        
        return dummy.bottom