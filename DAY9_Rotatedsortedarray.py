#modern binary search
class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# recursive binary search
class solution:
    def search(self, nums, target: int) -> int:
     
        def binary_search(left, right):
                    if left > right:
                        return -1
                    mid = (left + right) >> 1
                    if nums[mid] == target:
                        return mid
                    if nums[left] <= nums[mid]:
                        if nums[left] <= target < nums[mid]:
                            return binary_search(left, mid - 1)
                        else:
                            return binary_search(mid + 1, right)
                    else:
                        if nums[mid] < target <= nums[right]:
                            return binary_search(mid + 1, right)
                        else:
                            return binary_search(left, mid - 1)
        return binary_search(0, len(nums) - 1)