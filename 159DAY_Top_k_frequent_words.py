class Solution(object):
    def topKFrequent(self, words, k):
        word_count = Counter(words)
        sorted_words = sorted(word_count.keys(), key=lambda word: (-word_count[word], word))
        
        return sorted_words[:k]



from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words, k):
        word_count = Counter(words)
        heap = []
        for word, freq in word_count.items():
            heapq.heappush(heap, (-freq, word))
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result