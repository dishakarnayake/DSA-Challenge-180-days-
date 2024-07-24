# Counting Sort
class Solution(object):
    def sortColors(self, nums):
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1
        i = 0
        for j in range(3):
                while count[j] > 0:
                    nums[i] = j
                    i += 1
                    count[j] -= 1
# time complexity - O(n)
# space complexity - O(1)










# Three pointer technique
def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1






# In - Place Swap
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
        












# My Way of sorting

        blue = white = red = 0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            elif num == 2:
                blue += 1

        for i in range(len(nums)):
            if i < red:
                nums[i] = 0
            elif i < red + white:
                nums[i] = 1
            elif i < red + white + blue:
                nums[i] = 2
        