# Copy the next node value
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        # Copy the value of the next node to the current node
        node.val = node.next.val
        # Bypass the next node
        node.next = node.next.next








# Recursive Approach
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):

        # Base case: the next node is the node to delete
        if node.next and node.next.next is None:
            node.next = None
            return
        node.val = node.next.val
        deleteNode(node.next)