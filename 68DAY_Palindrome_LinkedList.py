# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Using a Stack
class Solution(object):
    def isPalindrome(self, head):
        stack = []
        current = head
        
        # Push all values onto the stack
        while current:
            stack.append(current.val)
            current = current.next
        
        # Check if the list is a palindrome
        current = head
        while current:
            if current.val != stack.pop():
                return False
            current = current.next
        
        return True
        


# Reversing the Second Half of the Linked List 
class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        # Find the middle of the linked list using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse the second half of the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        # Check if the first half matches the reversed second half
        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True



# Recursive Approach 
class Solution(object):
    def isPalindrome(self, head):
        self.front_pointer = head
        
        def recursively_check(current_node):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True
        
        return recursively_check(head)








 
