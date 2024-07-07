#brute force method
class Solution(object):
    def searchRange(self, nums, target):
        start, end = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                if start == -1:
                    start = i
                end = i
        return [start, end]
        
        
        
# optimal approach using binary search
class solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return start
        
        def find_last(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return end
        start = find_first(nums, target)
        end = find_last(nums, target)
        if start <= end:
            return [start, end]
        else:
            return [-1, -1]