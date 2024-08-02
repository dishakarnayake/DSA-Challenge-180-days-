#Brute Force method
class Solution:
    def countAndSay(self, n):
        out = "1"

        for _ in range(1, n):
            prev_char = out[0]
            count = 1
            tmp = ""
            for j in range(1, len(out)):
                if prev_char == out[j]:
                    count += 1
                else:
                    tmp += count.__str__() + prev_char
                    prev_char = out[j]
                    count = 1
            tmp += count.__str__() + prev_char
            out = tmp
        
        return out
# Time complexity: O(2 n)
#Space complexity: O(1)






# recursive Approach
class solution:
    beg="1"
    def str_com(self,s):
            tem=""
            cnt=1
            ref=self.beg+"0"
            for i in range(len(ref)-1):
                if ref[i]==ref[i+1]:
                    cnt+=1
                else:
                    tem=tem+str(cnt)+ref[i]
                    cnt=1
            return tem
    def countAndSay(self, n:int) -> str:
        if n==1:
            return self.beg
        self.beg=self.str_com(self.beg)
        return self.countAndSay(n-1)

#Time complexity: O(2N)
#Space complexity: O(N)