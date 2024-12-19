class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        n = len(nums)
        dp = nums[:]  # Initialize dp array with nums
        dq = deque()  # Store indices of `dp`
        max_sum = nums[0]

        for i in range(n):
            # Remove indices that are out of range
            if dq and dq[0] < i - k:
                dq.popleft()

            # Update dp[i] with the max value from the deque
            if dq:
                dp[i] += dp[dq[0]]

            # Update max_sum
            max_sum = max(max_sum, dp[i])

            # Maintain decreasing order in deque
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)

        return max_sum
        


class Solution:
    def constrainedSubsetSum(self, nums, k):
        n = len(nums)
        max_sum = float('-inf')

        # Generate all subsequences
        for size in range(1, n + 1):
            for subseq in combinations(range(n), size):
                if all(subseq[i + 1] - subseq[i] <= k for i in range(len(subseq) - 1)):
                    max_sum = max(max_sum, sum(nums[i] for i in subseq))

        return max_sum