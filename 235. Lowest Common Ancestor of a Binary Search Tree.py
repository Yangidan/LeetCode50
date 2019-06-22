# day 43 2019-06-21 Fri
# 235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        if q.val>node.val and p.val>node.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif q.val<node.val and p.val<node.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return node