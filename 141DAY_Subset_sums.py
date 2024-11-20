class Solution:
    def subsetSums(self, arr, n):
        def findSums(index, current_sum, result):
            if index == n:
                result.append(current_sum)
                return
            findSums(index + 1, current_sum + arr[index], result)

            findSums(index + 1, current_sum, result)
        
        result = []
        findSums(0, 0, result)
        return result




class Solution:
    def subsetSums(self, arr, n):
        result = []
        for i in range(1 << n):  # Loop from 0 to 2^n - 1
            subset_sum = 0
            for j in range(n):
                if i & (1 << j):  # Check if the j-th bit is set
                    subset_sum += arr[j]
            result.append(subset_sum)
        return result




class Solution:
    def subsetSums(self, arr, n):
        result = [0]  # Start with an empty subset
        for num in arr:
            new_sums = []
            for current_sum in result:
                new_sums.append(current_sum + num)
            result.extend(new_sums)
        return result