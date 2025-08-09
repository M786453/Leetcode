# 872. Leaf-Similar Trees
from collections import deque


class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def leafSequence(self, root, seq):

        if root is None:
            return seq

        if root.left is None and root.right is None:
            return [root.val]

        return self.leafSequence(root.left, seq) + self.leafSequence(root.right, seq)

    def leafSimilar(self, root1, root2):

        seq1 = self.leafSequence(root1, [])
        seq2 = self.leafSequence(root2, [])

        return seq1 == seq2


ss = Solution()

root1 = TreeNode(
    3,
    TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
    TreeNode(1, TreeNode(9), TreeNode(8)),
)

root2 = TreeNode(
    3,
    TreeNode(5, TreeNode(6), TreeNode(7)),
    TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))),
)

print("Answer:", ss.leafSimilar(root1, root2))
