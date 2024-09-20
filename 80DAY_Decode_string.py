# stack approach
class Solution(object):
    def decodeString(self, s):
        stack = []
        curr_num = 0
        curr_str = ""
        
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                # Push the current string and number to stack
                stack.append((curr_str, curr_num))
                # Reset the current string and number
                curr_str = ""
                curr_num = 0
            elif char == ']':
                # Pop from the stack and decode the substring
                prev_str, num = stack.pop()
                curr_str = prev_str + num * curr_str
            else:
                curr_str += char
        
        return curr_str
        

# recursive approach
class Solution:
    def decodeString(self, s):
        def decode(index):
            decoded_str = ""
            num = 0
            
            while index < len(s):
                if s[index].isdigit():
                    num = num * 10 + int(s[index])
                elif s[index] == '[':
                    index, sub_str = decode(index + 1)
                    decoded_str += num * sub_str
                    num = 0
                elif s[index] == ']':
                    return index, decoded_str
                else:
                    decoded_str += s[index]
                index += 1
                
            return decoded_str
        
        return decode(0)[1]


# optimized recursive approach
class Solution:
    def decodeString(self, s) :
        self.index = 0
        
        def decode():
            curr_str = ""
            num = 0
            
            while self.index < len(s):
                if s[self.index].isdigit():
                    num = num * 10 + int(s[self.index])
                elif s[self.index] == '[':
                    self.index += 1
                    sub_str = decode()
                    curr_str += num * sub_str
                    num = 0
                elif s[self.index] == ']':
                    return curr_str
                else:
                    curr_str += s[self.index]
                self.index += 1
            
            return curr_str
        
        return decode()
