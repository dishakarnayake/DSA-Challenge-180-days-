
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key=lambda x: x.profit, reverse=True)

        # Initialize result variables
        max_deadline = max(job.deadline for job in Jobs)
        slots = [-1] * (max_deadline + 1)  # Track occupied slots
        num_jobs = 0
        max_profit = 0

        # Iterate over sorted jobs
        for job in Jobs:
            for j in range(min(max_deadline, job.deadline), 0, -1):
                if slots[j] == -1:  # Check if slot is free
                    slots[j] = job.id
                    num_jobs += 1
                    max_profit += job.profit
                    break

        return [num_jobs, max_profit]
        # code here



class Solution:
    def find(self, parent, x):
        if parent[x] == x:
            return x
        parent[x] = self.find(parent, parent[x])  # Path compression
        return parent[x]

    def JobScheduling(self, Jobs, n):
        # Sort jobs in descending order of profit
        Jobs.sort(key=lambda x: x.profit, reverse=True)

        # Find the maximum deadline
        max_deadline = max(job.deadline for job in Jobs)

        # Initialize parent array for DSU
        parent = [i for i in range(max_deadline + 1)]

        num_jobs = 0
        max_profit = 0

        # Iterate over jobs
        for job in Jobs:
            # Find the latest available slot
            available_slot = self.find(parent, job.deadline)
            if available_slot > 0:  # If a valid slot exists
                parent[available_slot] = self.find(parent, available_slot - 1)  # Union
                num_jobs += 1
                max_profit += job.profit

        return [num_jobs, max_profit]




import heapq

class Solution:
    def JobScheduling(self, Jobs, n):
        # Sort jobs by deadline
        Jobs.sort(key=lambda x: x.deadline)

        # Min-heap to store profits
        min_heap = []
        max_profit = 0
        num_jobs = 0

        for job in Jobs:
            if len(min_heap) < job.deadline:
                heapq.heappush(min_heap, job.profit)
                max_profit += job.profit
                num_jobs += 1
            elif min_heap and job.profit > min_heap[0]:
                max_profit += job.profit - heapq.heappop(min_heap)
                heapq.heappush(min_heap, job.profit)

        return [num_jobs, max_profit]


