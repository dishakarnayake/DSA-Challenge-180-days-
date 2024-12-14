class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, min(i + indexDiff + 1, n)):
                if abs(nums[i] - nums[j]) <= valueDiff:
                    return True
        return False
        

from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        sorted_list = SortedList()
        
        for i in range(len(nums)):
            # Remove the element that is too far away
            if i > indexDiff:
                sorted_list.remove(nums[i - indexDiff - 1])
            
            # Check if any element in the sorted list satisfies the condition
            pos1 = SortedList.bisect_left(sorted_list, nums[i] - valueDiff)
            if pos1 < len(sorted_list) and abs(sorted_list[pos1] - nums[i]) <= valueDiff:
                return True
            
            # Add the current number to the sorted list
            sorted_list.add(nums[i])
        
        return False
