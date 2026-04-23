
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:

            return -1

        maximal_level = 0
        maximal_sum = float('-inf')

        que = deque([root])

        level = 1

        while que:

            level_size = len(que)

            level_sum = 0

            for i in range(level_size):

                node = que.popleft()

                level_sum += node.val

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            if level_sum > maximal_sum:

                maximal_sum = level_sum

                maximal_level = level

            level += 1

        return maximal_level

                    
s = Solution()

# root = TreeNode(1, TreeNode(7, TreeNode(0, None, None), TreeNode(7, None, None)), TreeNode(0, None, None))

root = TreeNode(989, None ,TreeNode(10250, TreeNode(98693, None, None), TreeNode(-89388, None, TreeNode(-32127, None, None))))

print("Answer:", s.maxLevelSum(root))