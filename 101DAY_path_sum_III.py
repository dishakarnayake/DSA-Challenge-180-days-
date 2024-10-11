class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return 0

        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val
            path_count = 1 if curr_sum == targetSum else 0

            path_count += dfs(node.left, curr_sum)
            path_count += dfs(node.right, curr_sum)

            return path_count
        return dfs(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)







class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return 0

        prefix_sum = {0: 1}

        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val
            path_count = prefix_sum.get(curr_sum - targetSum, 0)

            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

            path_count += dfs(node.left, curr_sum)
            path_count += dfs(node.right, curr_sum)

            prefix_sum[curr_sum] -= 1

            return path_count

        return dfs(root, 0)





class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return 0

        memo = {}

        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val
            path_count = memo.get((node, curr_sum), 0)

            if curr_sum == targetSum:
                path_count += 1

            path_count += dfs(node.left, curr_sum)
            path_count += dfs(node.right, curr_sum)

            memo[(node, curr_sum)] = path_count
            return path_count

        return dfs(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
