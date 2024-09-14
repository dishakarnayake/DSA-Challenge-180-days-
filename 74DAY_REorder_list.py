# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#using list to store nodes
class Solution(object):
    def reorderList(self, head):
        if not head:
            return
        
        # Step 1: Store all nodes in a list
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        # Step 2: Reorder the list using two pointers
        left, right = 0, len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            if left == right:
                break
            nodes[right].next = nodes[left]
            right -= 1
        
        nodes[left].next = None



# reverse the second half and merge
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: Merge the two halves
        first, second = head, prev
        while second.next:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

# Recursive approach
class Solution(object):
    def reorderList(self, head):
        def helper(left, right):
            if not right:
                return left
            
            left = helper(left, right.next)
            if left is None or left == right or left.next == right:
                return None
            
            temp = left.next
            left.next = right
            right.next = temp
            return temp
        
        helper(head, head)
        
        # Ensure the last node points to None
        temp = head
        while temp and temp.next:
            temp = temp.next
        if temp:
            temp.next = None
