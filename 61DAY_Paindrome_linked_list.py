# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#List to store values
class Solution(object):
    def isPalindrome(self, head):
        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next
        return vals == vals[::-1]
        
#Using a Fast and Slow Pointer (Reversing the Second Half)
class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        slow, fast = head, head
        
        # Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Compare the first and second halves
        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True


#Recursive Approach
class Solution(object):
    def isPalindrome(self, head):
        self.front_pointer = head
        
        def recursively_check(current):
            if current is not None:
                if not recursively_check(current.next):
                    return False
                if self.front_pointer.val != current.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True
        
        return recursively_check(head)

