# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random

class Solution(object):

    def __init__(self, head):
        self.head = head
    def getRandom(self):
        # Start with the head node
        current = self.head
        result = current.val
        i = 1
        # Traverse the linked list
        while current is not None:
            # Reservoir Sampling: Choose the current node with probability 1/i
            if random.randint(1, i) == 1:
                result = current.val
            current = current.next
            i += 1
        
        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()