# day 31 2019-06-09 Sun
# 124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# From 花花酱 https://www.youtube.com/watch?v=9ZNky1wqNUw
class Solution(object):
    def _maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return -sys.maxint
        
        l = max(0, self._maxPathSum(root.left))
        r = max(0, self._maxPathSum(root.right))
        self.ans = max(self.ans, root.val + l + r)
        return root.val + max(l,r)

    def maxPathSum(self, root):
        self.ans = -sys.maxint
        self._maxPathSum(root)
        return self.ans
class Solution(object):
    def _maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return -sys.maxint
        
        l = max(0, self._maxPathSum(root.left))
        r = max(0, self._maxPathSum(root.right))
        self.ans = max(self.ans, root.val + l + r)
        return root.val + max(l,r)

    def maxPathSum(self, root):
        self.ans = -sys.maxint
        self._maxPathSum(root)
        return self.ans