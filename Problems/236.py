# 236. Lowest Common Ancestor of a Binary Tree

class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):


    def lowestCommonAncestor(self, root, p, q):

        self.nodes_list = []

        def dfs(root):

            if root is None:
                return
            
            print("Val:", root.val)

            self.nodes_list.append(root.val)
            
            if root.val == p:
                print("Found p")
            elif root.val == q:
                print("Found q")

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        print(self.nodes_list)


if __name__ == "__main__":

    root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))

    ss = Solution()

    ss.lowestCommonAncestor(root, 5, 1)
            