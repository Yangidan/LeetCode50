# day 26 2019-06-04 Tue
# 104. Maximum Depth of Binary Tree

class Solution:
    def maxDepth(self, root):
        if root is None: 
            return 0 
        else: 
            left_D = self.maxDepth(root.left) 
            right_D = self.maxDepth(root.right) 
            return max(left_D, right_D) + 1 