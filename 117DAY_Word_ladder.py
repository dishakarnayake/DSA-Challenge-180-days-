from collections import deque
def shortestChainLen(start, target, D):
    
    if start == target:
      return 0
    if target not in D:
        return 0

    level, wordlength = 0, len(start)

    Q =  deque()
    Q.append(start)

    while (len(Q) > 0):
        
        level += 1

        sizeofQ = len(Q)

        for i in range(sizeofQ):

            word = [j for j in Q.popleft()]
            for pos in range(wordlength):
                
                orig_char = word[pos]

                for c in range(ord('a'), ord('z')+1):
                    word[pos] = chr(c)

                    if ("".join(word) == target):
                        return level + 1

                    if ("".join(word) not in D):
                        continue
                        
                    del D["".join(word)]

                    Q.append("".join(word))

                word[pos] = orig_char

    return 0

if __name__ == '__main__':
    
    D = {}
    D["poon"] = 1
    D["plee"] = 1
    D["same"] = 1
    D["poie"] = 1
    D["plie"] = 1
    D["poin"] = 1
    D["plea"] = 1
    start = "toon"
    target = "plea"
    
    print("Length of shortest chain is: ",
    shortestChainLen(start, target, D))
    
    
    
    

    
from typing import List, Tuple, Set, Dict, Any, Union

def shortest_chain_len(start: str, target: str, D: Set[str]) -> int:
    if start == target:
        return 0

    umap: Dict[str, List[str]] = {}

    for i in range(len(start)):
        intermediate_word = start[:i] + "*" + start[i+1:]
        umap[intermediate_word] = []

    for word in D:
        for i in range(len(word)):
            intermediate_word = word[:i] + "*" + word[i+1:]
            if intermediate_word not in umap:
                umap[intermediate_word] = []
            umap[intermediate_word].append(word)

    q = [(start, 1)]
    visited = {start: 1}
    while q:
        word, dist = q.pop(0)

        if word == target:
            return dist

        for i in range(len(word)):
            intermediate_word = word[:i] + '*' + word[i+1:]
            vect = umap[intermediate_word]
            for k in range(len(vect)):
              
                if vect[k] not in visited:
                    visited[vect[k]] = 1
                    q.append((vect[k], dist + 1))

    return 0

D = {'poon', 'plee', 'same', 'poie', 'plie', 'poin', 'plea'}
start = "toon"
target = "plea"
print(f"Length of shortest chain is: {shortest_chain_len(start, target, D)}")