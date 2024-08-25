# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Approach 1: Floyd’s Tortoise and Hare (Cycle Detection)
class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        
        # Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        # If there is no cycle
        if not fast or not fast.next:
            return None
        
        # Find the start of the cycle
        ptr = head
        while ptr != slow:
            ptr = ptr.next
            slow = slow.next
        
        return ptr






#Approach 2: HashSet
class Solution(object):
    def detectCycle(self, head):
        visited = set()
        current = head
        
        while current:
            if current in visited:
                return current
            visited.add(current)
            current = current.next
        
        return None









        