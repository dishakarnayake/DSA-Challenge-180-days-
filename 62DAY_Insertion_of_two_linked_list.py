# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Brute Force
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        currentA = headA
        while currentA:
            currentB = headB
            while currentB:
                if currentA == currentB:
                    return currentA
                currentB = currentB.next
            currentA = currentA.next
        return None



# Hash Set
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        visited = set()
        currentA = headA
        while currentA:
            visited.add(currentA)
            currentA = currentA.next
            
        currentB = headB
        while currentB:
            if currentB in visited:
                return currentB
            currentB = currentB.next
        return None


# Two Pointers
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        pointerA, pointerB = headA, headB
        
        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        return pointerA


# Length Difference
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        lengthA, lengthB = getLength(headA), getLength(headB)
        
        # Align both lists
        while lengthA > lengthB:
            headA = headA.next
            lengthA -= 1
        while lengthB > lengthA:
            headB = headB.next
            lengthB -= 1
            
        # Traverse together
        while headA != headB:
            headA = headA.next
            headB = headB.next
            
        return headA

        