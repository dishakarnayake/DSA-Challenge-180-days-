
# Two pointer approach
def twoSum(self, nums, target):
    nums_sorted = sorted((num, i) for i, num in enumerate(nums))  # Sort the list of numbers with their indices
    left, right = 0, len(nums_sorted) - 1  # Initialize two pointers, one at the start and one at the end

    while left < right:
        current_sum = nums_sorted[left][0] + nums_sorted[right][0]  # Calculate the sum of the numbers at the two pointers
        if current_sum == target:
                return [nums_sorted[left][1], nums_sorted[right][1]]  # Return the indices of the two numbers
        elif current_sum < target:
                left += 1  # Move the left pointer to the right
        else:
                right -= 1  # Move the right pointer to the left

        return []  # Return an empty list if no solution is found
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # Output: [0, 1]




# Using Hashing
def two_sum(nums, target):
    num_map = {}  # Create an empty hashmap

    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement of the current number
        if complement in num_map:  # Check if the complement is already in the hashmap
            return [num_map[complement], i]  # Return the indices of the two numbers
        num_map[num] = i  # Add the current number to the hashmap

    return []  # Return an empty list if no solution is found
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]




# Brute force method
def two_Sum(nums, target):
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []  # Return an empty list if no solution is found
nums = [2, 7, 11, 15]
target = 9
result = two_Sum(nums, target)
print(result)  # Output: [0, 1]