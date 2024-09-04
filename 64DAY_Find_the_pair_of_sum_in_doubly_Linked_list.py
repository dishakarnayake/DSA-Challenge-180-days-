from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""
# Two pointer approach
class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
         # Initialize the list to store the pairs
        result = []
        
        # Two pointers: left starting from the head, right starting from the end
        left = head
        right = head
        
        # Move the right pointer to the end of the list
        while right.next:
            right = right.next
        
        # Traverse the list from both ends until the two pointers meet
        while left != right and left.prev != right:
            current_sum = left.data + right.data
            
            # If sum of left and right is equal to target, add to result
            if current_sum == target:
                result.append([left.data, right.data])
                left = left.next
                right = right.prev
            
            # If current sum is less than target, move the left pointer to the right
            elif current_sum < target:
                left = left.next
            
            # If current sum is greater than target, move the right pointer to the left
            else:
                right = right.prev
        
        return result
        
# hashing 

class Solution:
    def findPairsWithGivenSum(self, target, head) :
        # Initialize a hash set to store the visited nodes' data
        seen = set()
        result = []
        
        # Traverse the doubly linked list
        current = head
        while current:
            # Calculate the complement
            complement = target - current.data
            
            # If the complement exists in the set, we found a pair
            if complement in seen:
                result.append([complement, current.data])
            
            # Add the current node's data to the set
            seen.add(current.data)
            
            # Move to the next node
            current = current.next
        
        return result
        
        
        
        
        
        
        
        
        
# Brute force method

class Solution:
    def findPairsWithGivenSum(self, target, head) :
        result = []
        
        # Outer loop to pick each node as the first element of the pair
        current = head
        while current:
            # Inner loop to pick each node as the second element of the pair
            next_node = current.next
            while next_node:
                # Check if the sum of the current pair equals the target
                if current.data + next_node.data == target:
                    result.append([current.data, next_node.data])
                next_node = next_node.next
            
            current = current.next
        
        return result
        
        