class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        answer = []
        for k, trim in queries:
            # Trim each number to its last `trim` digits
            trimmed = [(num[-trim:], i) for i, num in enumerate(nums)]
            # Sort by the trimmed number, breaking ties using the original index
            trimmed.sort()
            # Find the index of the k-th smallest trimmed number
            answer.append(trimmed[k - 1][1])
        return answer
        