from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort()

        dq = deque()

        
        for card in reversed(deck):
            if dq:
                dq.appendleft(card)
        return list(dq)




class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort()

       
        n = len(deck)
        indices = list(range(n))

        result = [0] * n

        
        for card in deck:
            result[indices.pop(0)] = card  
            if indices: 
                indices.append(indices.pop(0))

        return result

