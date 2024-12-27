class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        n = len(nums)
        mid = (n - 1) // 2  
        
        result = [0] * n
        left, right = mid, n - 1  
        
        for i in range(n):
            if i % 2 == 0:
                result[i] = nums[left]
                left -= 1
            else:
                result[i] = nums[right]
                right -= 1
        
        nums[:] = result  

class Solution:
    def wiggleSort(self, nums):
        n = len(nums)
        nums.sort()
        
        def virtual_index(i):
            return (2 * i + 1) % (n | 1)  
        
        mid_val = nums[(n - 1) // 2] 
        left, right, i = 0, n - 1, 0
        
        while i <= right:
            vi = virtual_index(i)
            if nums[vi] > mid_val:
                nums[virtual_index(left)], nums[vi] = nums[vi], nums[virtual_index(left)]
                left += 1
                i += 1
            elif nums[vi] < mid_val:
                nums[virtual_index(right)], nums[vi] = nums[vi], nums[virtual_index(right)]
                right -= 1
            else:
                i += 1

class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        n = len(nums)
        mid = (n - 1) // 2
        
        smaller_half = nums[:mid + 1]
        larger_half = nums[mid + 1:]
        
        smaller_half = smaller_half[::-1]
        larger_half = larger_half[::-1]
        
        i, j, k = 0, 0, 0
        while i < len(smaller_half) or j < len(larger_half):
            if i < len(smaller_half):
                nums[k] = smaller_half[i]
                i += 1
                k += 1
            if j < len(larger_half):
                nums[k] = larger_half[j]
                j += 1
                k += 1
