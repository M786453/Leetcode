# 437. Path Sum III
from collections import deque

class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution(object):

    def pathSum(self, root, targetSum):

        self.count = 0
        prefix_sum_count = {0: 1}  # base case: one way to have sum 0

        def dfs(node, current_sum):
            if not node:
                return
            # update current sum
            current_sum += node.val

            # check if there is a subpath ending here that sums to target
            self.count += prefix_sum_count.get(current_sum - targetSum, 0)

            # update hashmap
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

            # recurse
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # backtrack
            prefix_sum_count[current_sum] -= 1

        dfs(root, 0)
        return self.count
        

if __name__ == "__main__":

    ss = Solution()

    root = TreeNode(-2, None, TreeNode(-3))

    targetSum = -5

    print("Answer:",ss.pathSum(root, targetSum))



