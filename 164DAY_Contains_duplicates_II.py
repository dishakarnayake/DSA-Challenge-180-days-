class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, min(i + k + 1, n)):
                if nums[i] == nums[j]:
                    return True
        return False



class Solution:
    def containsNearbyDuplicate(self, nums, k):
        index_map = {}
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i
        return False



class Solution:
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[i - k])
        return False
        