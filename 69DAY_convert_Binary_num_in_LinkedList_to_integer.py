# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# using bit shifting
class Solution(object):
    def getDecimalValue(self, head):
        result = 0
        while head:
            result = (result << 1) | head.val
            head = head.next
        return result
        
# convert to string
class Solution(object):
    def getDecimalValue(self, head):
        binary_str = ""
        while head:
            binary_str += str(head.val)
            head = head.next
        return int(binary_str, 2)

#recursive solution
class Solution(object):
    def getDecimalValue(self, head, result=0):
        if not head:
            return result
        return self.getDecimalValue(head.next, (result << 1) | head.val)
