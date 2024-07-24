# Brute force method

def maxProduct(nums: List[int]) -> int:
    max_product = float('-inf')
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            max_product = max(max_product, product)
    return max_product  

 # dynamic programming
def maxProduct(nums: List[int]) -> int:
    if not nums:
        return 0
    max_product = min_product = result = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        result = max(result, max_product)
    return result

# Kadane's aLgorithm
def maxProduct(nums: List[int]) -> int:
    if not nums:
        return 0
    max_product = min_product = result = nums[0]
    for i in range(1, len(nums)):
        temp = max_product
        max_product = max(nums[i], max_product * nums[i], min_product * nums[i])
        min_product = min(nums[i], temp * nums[i], min_product * nums[i])
        result = max(result, max_product)
    return result


# using numpy
import numpy as np

def maxProduct(nums: List[int]) -> int:
    return np.max(np.cumprod(nums))