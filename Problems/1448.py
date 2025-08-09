# 1448. Count Good Nodes in Binary Tree

class TreeNode:

    def __init__(self, val= 0, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def goodNodes(self, root):

        self.count = 0
        self.max_val = float('-inf')

        def dfs(root):

            if root is None:
                return
            
            old_max = self.max_val

            if root.val >= self.max_val:
                self.max_val = root.val
                self.count += 1

            dfs(root.left)
            dfs(root.right)

            self.max_val = old_max
        
        dfs(root)
        
        return self.count
    
ss = Solution()

root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))

print("Answer:",ss.goodNodes(root))
    

        

        

            


