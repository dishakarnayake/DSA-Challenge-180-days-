class MapSum(object):

    def __init__(self):
        self.map = {}
        

    def insert(self, key, val):
        self.map[key] = val
        

    def sum(self, prefix):
        return sum(val for k, val in self.map.items() if k.startswith(prefix))



class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key, val) :
        diff = val - self.map.get(key, 0)
        self.map[key] = val
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.value += diff

    def sum(self, prefix) :
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.value