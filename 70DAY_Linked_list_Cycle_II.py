# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Floyd Cycle Detection Algo
class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Cycle detected
                break
        else:
            return None  # No cycle
        
        # Reset slow to head and move both pointers one step at a time
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow  # Start of the cycle
        





# using Hashset
class Solution:
    def detectCycle(self, head):
        visited = set()
        while head:
            if head in visited:
                return head  # Start of the cycle
            visited.add(head)
            head = head.next
        return None  # No cycle














