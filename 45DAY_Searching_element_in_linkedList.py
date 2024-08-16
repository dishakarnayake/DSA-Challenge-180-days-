
# 1. Iterative Approach
class Solution:
    def searchKey(self, n, head, key):
        current = head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    
# 2. Recursive Approach
class S_olution:
    def searchKey(self, n, head, key):
        if head is None:
            return False
        if head.data == key:
            return True
        return self.searchKey(n, head.next, key)

# 3. Hash Set Approach (for frequent searches)
class So_lution:
    def __init__(self):
        self.node_set = set()
    
    def preprocess(self, head):
        current = head
        while current:
            self.node_set.add(current.data)
            current = current.next
    
    def searchKey(self, n, head, key):
        if not self.node_set:  # Preprocess if not already done
            self.preprocess(head)
        return key in self.node_set