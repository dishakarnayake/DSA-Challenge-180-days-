from collections import deque

class Solution:
    def countStudents(self, students, sandwiches):
        student_queue = deque(students)
        sandwich_stack = sandwiches
        count = 0  
        
        while student_queue and count < len(student_queue):
            if student_queue[0] == sandwich_stack[0]:  
                student_queue.popleft()  
                sandwich_stack.pop(0)    
                count = 0  
            else:
                student_queue.append(student_queue.popleft())  
                count += 1  
                
        return len(student_queue)









class Solution:
    def countStudents(self, students, sandwiches):
        count0 = students.count(0)  
        count1 = students.count(1) 
        
   
        for s in sandwiches:
            if s == 0:
                if count0 > 0:
                    count0 -= 1 
                else:
                    return count0 + count1  
            else:
                if count1 > 0:
                    count1 -= 1  
                else:
                    return count0 + count1  
        
        return 0 






