# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# iterative approach
class Solution(object):
    def reverseKGroup(self, head, k):
        if head is None or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        tail = dummy
        
        while True:
            count = 0
            while tail and count < k:
                tail = tail.next
                count += 1
            
            if not tail:
                break
            
            head_next = prev.next
            cur = prev.next
            
            for _ in range(k - 1):
                temp = cur.next
                cur.next = temp.next
                temp.next = prev.next
                prev.next = temp
            
            prev = head_next
            tail = prev
            
        return dummy.next
        



#Recursive approach
class Solution:
    def reverseKGroup(self, head, k):
        count = 0
        node = head
        
        # Check if there are at least k nodes left
        while node and count < k:
            node = node.next
            count += 1
        
        if count == k:
            reversed_head = self.reverse(head, k)
            head.next = self.reverseKGroup(node, k)
            return reversed_head
        return head
    
    def reverse(self, head, k):
        prev = None
        current = head
        while k > 0:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            k -= 1
        return prev

#using stack
class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        stack = []
        
        while True:
            count = 0
            temp = head
            
            while temp and count < k:
                stack.append(temp)
                temp = temp.next
                count += 1
            
            if count < k:
                prev.next = head
                break
            
            while stack:
                prev.next = stack.pop()
                prev = prev.next
            
            prev.next = temp
            head = temp
        
        return dummy.next
