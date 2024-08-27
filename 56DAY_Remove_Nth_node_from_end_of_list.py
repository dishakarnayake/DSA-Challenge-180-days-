# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Two pass method
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Step 1: Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Find the (length-n)th node
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        for _ in range(length - n):
            current = current.next
        
        # Remove the nth node
        current.next = current.next.next
        
        return dummy.next
        



        
#one- pass with two pointer
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Initialize dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Remove the nth node from end
        second.next = second.next.next
        
        return dummy.next
