class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def atMost(k):
            count = 0
            left = 0
            odd_count = 0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:  # Count odd numbers
                    k -= 1
                while k < 0:
                    if nums[left] % 2 == 1:
                        k += 1
                    left += 1
                count += right - left + 1
            return count
        
        return atMost(k) - atMost(k - 1)
        

class Solution:
    def numberOfSubarrays(self, nums, k):
        count = 0
        odd_count = 0
        prefix_count = {0: 1}  # To handle the case when odd_count == k
        
        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            if odd_count - k in prefix_count:
                count += prefix_count[odd_count - k]
            prefix_count[odd_count] = prefix_count.get(odd_count, 0) + 1
        
        return count
