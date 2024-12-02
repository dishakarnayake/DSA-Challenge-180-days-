class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                max_xor = max(max_xor, nums[i] ^ nums[j])
        return max_xor



class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def findMaximumXOR(self, nums):
        # Build Trie
        root = TrieNode()
        for num in nums:
            node = root
            for bit in format(num, '032b'):  # Convert number to 32-bit binary
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        # Find max XOR
        max_xor = 0
        for num in nums:
            node = root
            curr_xor = 0
            for bit in format(num, '032b'):
                # Choose the opposite bit if it exists
                opposite_bit = '1' if bit == '0' else '0'
                if opposite_bit in node.children:
                    curr_xor = (curr_xor << 1) | 1
                    node = node.children[opposite_bit]
                else:
                    curr_xor = (curr_xor << 1)
                    node = node.children[bit]
            max_xor = max(max_xor, curr_xor)
        return max_xor



class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):  # Check from MSB to LSB
            mask |= (1 << i)
            prefixes = {num & mask for num in nums}
            temp = max_xor | (1 << i)
            if any(temp ^ prefix in prefixes for prefix in prefixes):
                max_xor = temp
        return max_xor


