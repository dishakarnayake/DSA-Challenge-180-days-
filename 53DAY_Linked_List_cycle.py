# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Floyd’s Tortoise and Hare (Cycle Detection) Algorithm
class Solution(object):
    def hasCycle(self, head):
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
        

# hash table
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        current = head
        
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        
        return False



# Modified Linked List
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if head.val == 'visited':
                return True
            head.val = 'visited'
            head = head.next
            
        return False
