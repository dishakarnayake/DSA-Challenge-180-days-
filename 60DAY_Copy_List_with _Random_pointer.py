

# using hash map
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Dictionary to map original nodes to their copies
        old_to_new = {}

        # First pass: create copies of all the nodes
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Second pass: assign next and random pointers
        current = head
        while current:
            old_to_new[current].next = old_to_new.get(current.next)
            old_to_new[current].random = old_to_new.get(current.random)
            current = current.next

        return old_to_new[head]

# interweaving node
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # First pass: interleave copied nodes with original nodes
        current = head
        while current:
            new_node = Node(current.val, current.next, None)
            current.next = new_node
            current = new_node.next

        # Second pass: assign random pointers
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Third pass: restore the original list and extract the copy
        current = head
        copy_head = head.next
        while current:
            copy = current.next
            current.next = copy.next
            current = current.next
            if current:
                copy.next = current.next

        return copy_head

#recursive Approach With hash map
class Solution:
    def __init__(self):
        # Dictionary to hold the old nodes and their copies
        self.visited = {}

    def copyRandomList(self, head):
        if not head:
            return None

        # If the node is already copied, return its copy
        if head in self.visited:
            return self.visited[head]

        # Create a new node with the value of the old node
        new_node = Node(head.val, None, None)
        self.visited[head] = new_node

        # Recursively copy the next and random nodes
        new_node.next = self.copyRandomList(head.next)
        new_node.random = self.copyRandomList(head.random)

        return new_node





class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        node_map = {}
        current = head
        
        # First pass: Create a copy of each node and store it in the map
        while current:
            node_map[current] = Node(current.val)
            current = current.next
        
        current = head
        
        # Second pass: Connect the copied nodes' next and random pointers
        while current:
            copy_node = node_map[current]
            copy_node.next = node_map.get(current.next)
            copy_node.random = node_map.get(current.random)
            current = current.next
        
        return node_map[head]