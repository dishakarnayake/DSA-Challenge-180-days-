# using stack
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for i in s:
            if len(s_stack)!=0:
                if i=='#':
                    s_stack.pop()
                    continue
            elif i=='#':
                continue
            s_stack.append(i)
        for i in t:
            if len(t_stack)!=0:
                if i=='#':
                    t_stack.pop()
                    continue
            elif i=='#':
                continue
            t_stack.append(i)
        
        if s_stack == t_stack:
            return True
        else:
            return False

        
# using slicing
class solution:
    def BackspaceCompare(self, s: str, t: str) -> bool:
        a=b=''
        for i in s:
            if i!='#':
                a+=i
            else:
                a=a[:-1:]
        for j in t:
            if j!='#':
                b+=j
            else:
                b=b[:-1:]
        return a==b