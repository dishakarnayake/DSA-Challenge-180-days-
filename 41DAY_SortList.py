
# Merge Sort (Top - Down)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        # Step 1: Split the list into two halves
        mid = self.getMid(head)
        left = head
        right = mid.next
        mid.next = None
        
        # Step 2: Sort each half
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Step 3: Merge the sorted halves
        return self.merge(left, right)
    
    def getMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next





#Merge sort (Bottom- UP)
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        # Get the length of the linked list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        dummy = ListNode(0)
        dummy.next = head
        size = 1
        
        while size < length:
            curr = dummy.next
            tail = dummy
            while curr:
                left = curr
                right = self.split(left, size)
                curr = self.split(right, size)
                tail = self.merge(left, right, tail)
            size *= 2
        
        return dummy.next
    
    def split(self, head, size):
        for i in range(1, size):
            if head and head.next:
                head = head.next
            else:
                return None
        if not head:
            return None
        next_head = head.next
        head.next = None
        return next_head
    
    def merge(self, l1, l2, tail):
        curr = tail
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        while curr.next:
            curr = curr.next
        return curr




# Insertion Sort
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        sorted_head = ListNode(0)  # Dummy node for the sorted part
        curr = head
        
        while curr:
            prev = sorted_head
            next = curr.next
            
            # Find the correct position to insert the current node
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # Insert the current node
            curr.next = prev.next
            prev.next = curr
            
            # Move to the next node
            curr = next
        
        return sorted_head.next
