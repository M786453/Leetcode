# 1448. Count Good Nodes in Binary Tree

class TreeNode:

    def __init__(self, val= 0, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def goodNodes(self, root):

        count = 0

        if root is None:
            return count

        def dfs(root, max_val, count):

            if root is None:
                return count
            
            if root.val >= max_val:
                max_val = root.val
                count += 1

            count = dfs(root.left, max_val, count)
            count = dfs(root.right, max_val, count)

            return count
        
        count = dfs(root, float('-inf'), count)
        
        return count
    
ss = Solution()

root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))

print("Answer:",ss.goodNodes(root))
    

        

        

            


