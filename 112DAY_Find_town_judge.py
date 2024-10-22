class Solution:
    def findJudge(self, n, trust):
        if n == 1 and not trust:
            return 1

        trust_count = [0] * (n + 1)
        trusted_by = [0] * (n + 1)
        
        for a, b in trust:
            trust_count[b] += 1  
            trusted_by[a] += 1  

        for i in range(1, n + 1):
            if trust_count[i] == n - 1 and trusted_by[i] == 0:
                return i
        return -1




class Solution:
    def findJudge(self, n, trust):
        if n == 1 and not trust:
            return 1
        
        score = [0] * (n + 1)
        
        for a, b in trust:
            score[a] -= 1 
            score[b] += 1  
        
        for i in range(1, n + 1):
            if score[i] == n - 1:  
                return i
        
        return -1




from collections import defaultdict

class Solution:
    def findJudge(self, n, trust):
        if n == 1 and not trust:
            return 1

        graph = defaultdict(list)
        
        for a, b in trust:
            graph[a].append(b)
        
        candidates = []
        for i in range(1, n + 1):
            if i not in graph:  
                candidates.append(i)
        
        for candidate in candidates:
            count_trusted = sum(1 for a, b in trust if b == candidate)
            if count_trusted == n - 1:
                return candidate
        
        return -1
