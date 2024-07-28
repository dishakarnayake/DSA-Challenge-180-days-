from typing import List
from collections import defaultdict

# using hashmap
class Solution:
    def getSignature(self, s: str) -> str:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        result = []
        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a')), str(count[i])])

        return ''.join(result)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        groups = defaultdict(list)

        for s in strs:
            groups[self.getSignature(s)].append(s)

        result.extend(groups.values())

        return result

obj = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(obj.groupAnagrams(strs))
# time complexity O(n)
# space complexity O(n)




# using collections
class solution(object):
    def groupAnagrams(self,strs):
        h= defaultdict(list)
        k=""
        for you in strs:
            s = k.join(sorted(you))
            h[s].append(you)
        return sorted(h.values())
obj = solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(obj.groupAnagrams(strs))
# time complexity O(n)
# space complexity O(n)