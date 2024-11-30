class Trie(object):

    def __init__(self):
        self.root = {}

    def insert(self, word) :
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True  # Mark the end of a word

    def search(self, word) :
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '#' in node  # Check if it is a complete word

    def startsWith(self, prefix) :
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False




class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word) :
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word) :
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix) :
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
