
# by using slicing
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))
    
# time complexity O(n)
# space complexity O(n)




# by using stack
class solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.lower()
        print(s)
        for i in s:
            if i.isalnum()==False:
                s=s.replace(i,"")
        return s==s[::-1]
# time complexity O(n)
# space complexity O(n)



# by using reverse
class S_olution:
    def isPalindrome(self, s: str) -> bool:
        trimmed_str = ''.join(c.lower() for c in s if c.isalnum())
        return trimmed_str == trimmed_str[::-1]
# time complexity O(n)
# space complexity O(n)