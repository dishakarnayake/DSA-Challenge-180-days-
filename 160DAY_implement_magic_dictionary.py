class MagicDictionary:

    def __init__(self):
        self.words = []

    def buildDict(self, dictionary):
        self.words = dictionary

    def search(self, searchWord):
        for word in self.words:
            if len(word) != len(searchWord):
                continue
            mismatch_count = 0
            for a, b in zip(word, searchWord):
                if a != b:
                    mismatch_count += 1
                if mismatch_count > 1:
                    break
            if mismatch_count == 1:
                return True
        return False


from collections import defaultdict

class MagicDictionary:

    def __init__(self):
        self.length_dict = defaultdict(list)

    def buildDict(self, dictionary):
        for word in dictionary:
            self.length_dict[len(word)].append(word)

    def search(self, searchWord):
        length = len(searchWord)
        if length not in self.length_dict:
            return False

        for word in self.length_dict[length]:
            mismatch_count = 0
            for a, b in zip(word, searchWord):
                if a != b:
                    mismatch_count += 1
                if mismatch_count > 1:
                    break
            if mismatch_count == 1:
                return True
        return False



