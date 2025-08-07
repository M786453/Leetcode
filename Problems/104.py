# 104. Maximum Depth of Binary Tree

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:

    # DFS
    def maxDepth(self, root):

        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
if __name__ == "__main__":

    root = TreeNode(1)

    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.left.left = TreeNode(15)
    root.left.right = TreeNode(13)

    root.right.right = TreeNode(6)
    # root.right.right = TreeNode(7)

    ss = Solution()

    print("Answer:", ss.maxDepth(root))
