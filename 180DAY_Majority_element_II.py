class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        threshold = n // 3
        result = []
        
        for num in set(nums):
            if nums.count(num) > threshold:
                result.append(num)
        
        return result


class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        threshold = n // 3
        count = {}
        result = []
        
        # Count occurrences of each element
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Add elements that exceed threshold
        for num, freq in count.items():
            if freq > threshold:
                result.append(num)
        
        return result