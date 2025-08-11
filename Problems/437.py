# 437. Path Sum III
from collections import deque

class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution(object):

    def pathSum(self, root, targetSum):

        self.q = deque()
        self.targetSum = targetSum
        self.count = 0

        def dfs(root):

            if root is None:
                return
            
            self.q.append(root.val)

            old_q = deque(self.q)

            print("sum:", sum(self.q))

            while self.q and sum(self.q) > self.targetSum:

                self.q.popleft()

            if self.q and sum(self.q) == self.targetSum:
                self.count += 1

            dfs(root.left)
            if old_q:
                old_q.pop()
            dfs(root.right)

            self.q = old_q
        
        dfs(root)
        
        return self.count

if __name__ == "__main__":

    ss = Solution()

    root = TreeNode(-2, None, TreeNode(-3))

    targetSum = -5

    print("Answer:",ss.pathSum(root, targetSum))



