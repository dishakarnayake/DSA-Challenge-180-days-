# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        def buildBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(values[mid])
            node.left = buildBST(left, mid - 1)
            node.right = buildBST(mid + 1, right)
            return node
        
        return buildBST(0, len(values) - 1)




class Solution:
    def sortedListToBST(self, head):
       
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        def findMiddle(prev, slow, fast):
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None  
            return slow

        prev, slow, fast = None, head, head
        mid = findMiddle(prev, slow, fast)
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)  
        root.right = self.sortedListToBST(mid.next)  
        
        return root



        