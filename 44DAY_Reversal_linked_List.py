# iterative Reversal
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        # Dummy node to handle edge cases like reversing from head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node before the start of the sublist
        for _ in range(left - 1):
            prev = prev.next
        
        # Reverse the sublist
        current = prev.next
        next_node = None
        
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next
       




# Recursive Reversal
class Solution:
    def reverseBetween(self, head, left, right):  
        if left == 1:
            return self.reverseN(head, right)
        
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
    
    def reverseN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head
        
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # slow = head
        # new_head = ListNode(None, None)
        # new_head.next = head
        # left_edge = ListNode(None, None)
        # left_head = ListNode(None, None)
        # prev = ListNode(None, None)
        # trans = ListNode(None, None)
        
        # if head.next is None or left == right:
        #     return head

        # if left == 1:
        #     slow = new_head
        #     left_edge = slow
        #     for i in range(left-1):
        #         left_edge = slow
        #         slow=slow.next
        #     slow=slow.next
        #     left_head = slow
            
        #     trans=slow.next
        #     while (right-left):
        #         prev = slow
        #         slow = trans
        #         trans = slow.next
        #         slow.next = prev
        #         right-=1
            
        #     left_edge.next=slow
        #     left_head.next=trans

        #     return new_head.next

        # left_edge = slow
        # for i in range(left-2):
        #     slow=slow.next
        #     left_edge = slow
        # slow=slow.next
        # left_head = slow
        
        # trans=slow.next
        # while (right-left):
        #     prev = slow
        #     slow = trans
        #     trans = slow.next
        #     slow.next = prev
        #     right-=1
        
        # left_edge.next=slow
        # left_head.next=trans

        # return head
