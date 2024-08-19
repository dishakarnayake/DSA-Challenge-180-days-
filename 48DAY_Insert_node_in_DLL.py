# Your task is to complete this function
# function should add a new node after the pth position
# function shouldn't print or return any data

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''
#Function to insert a new node at given position in doubly linked list.
# iterative approach
def addNode(head, p, data):
    # Code here
    # If the list is empty, return the original head
    if not head:
        return head
    
    # Traverse the list to find the p-th node
    current = head
    for i in range(p):
        if current.next is None:
            return head  # If p is greater than the length of the list, return the original head
        current = current.next
    
    # Create the new node with the given data
    new_node = Node(data)
    
    # Adjust the pointers to insert the new node after the p-th node
    new_node.next = current.next
    if current.next:
        current.next.prev = new_node
    current.next = new_node
    new_node.prev = current
    
    return head
    
# Recursive Approach
def addNodeRecursive(current, p, data):
    if p == 0:
        new_node = Node(data)
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current
    else:
        addNodeRecursive(current.next, p - 1, data)

def addNode(head, p, data):
    # If the list is empty, return the original head
    if not head:
        return head
    
    addNodeRecursive(head, p, data)
    return head
