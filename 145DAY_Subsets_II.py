x  class Solution:
    def subsetsWithDup(self, nums):
        def backtrack(start, path):
            result.append(list(path))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        nums.sort()  
        result = []
        backtrack(0, [])
        return result



class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        result = [[]]
        start_idx = 0
        for i in range(len(nums)):
            start = start_idx if i > 0 and nums[i] == nums[i - 1] else 0
            start_idx = len(result)
            for j in range(start, len(result)):
                result.append(result[j] + [nums[i]])
        return result




class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        result = {tuple()}  
        for num in nums:
            new_subsets = {subset + (num,) for subset in result}
            result.update(new_subsets)
        
        return [list(subset) for subset in result]


