class Solution(object):
    def canSeePersonsCount(self, heights):
        n = len(heights)
        answer = [0] * n
        for i in range(n):
            count = 0
            for j in range(i + 1, n):
                if heights[j] > heights[i]:
                    count += 1
                    break 
                count += 1
            answer[i] = count
        
        return answer



class Solution(object):
    def canSeePersonsCount(self, heights):
        n = len(heights)
        answer = [0] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            count = 0
            
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1
            
            if stack:
                count += 1
            
            answer[i] = count
            
            stack.append(heights[i])
        
        return answer

        