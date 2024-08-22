# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Approach 1: Two-Pointer (Tortoise and Hare) Technique
class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
# Approach 2: Single Pass with Length Calculation
class Solution(object):
    def middleNode(self, head):
        length = 0
        current = head
        
        # First pass to calculate the length
        while current:
            length += 1
            current = current.next
        
        # Second pass to find the middle node
        middle_index = length // 2
        current = head
        
        for _ in range(middle_index):
            current = current.next
            
        return current



#Approach 3: Convert to List (Array-Based)
class Solution(object):
    def middleNode(self, head):
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        return nodes[len(nodes) // 2]
