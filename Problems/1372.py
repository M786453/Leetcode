# 1372. Longest ZigZag Path in a Binary Tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):

    def longestZigZag(self, root):

        self.longest_zig_zag_path = 0

        def zigzag(root, direction, nodes_count):

            if root is None:
                return
            
            self.longest_zig_zag_path = max(self.longest_zig_zag_path, nodes_count)
            
            if direction is "left":

                zigzag(root.right, "right", nodes_count+1)
                zigzag(root.left, "left", 1)
            
            else:

                zigzag(root.left, "left", nodes_count + 1)
                zigzag(root.right, "right", 1)

        zigzag(root.left, "left", 1)
        zigzag(root.right, "right", 1)

        return self.longest_zig_zag_path
        