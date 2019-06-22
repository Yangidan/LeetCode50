# day 44 2019-06-22 Sat
# 236. Lowest Common Ancestor of a Binary Tree

""" 参考 https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/comments/ """
# public class Solution {//所有的递归的返回值有4种可能性，null、p、q、公共祖先
#     public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
#         if (root == null) {//当遍历到叶结点后就会返回null
#             return root;
#         }
#         if (root == p || root == q) {//当找到p或者q的是时候就会返回pq
#             return root;/*当然，值得一提的是，如果公共祖先是自己（pq），并不需要寻找另外
#                      一个，我们在执行前序遍历会先找上面的，后找下面的，我们会直接返回公共祖先。*/
#         }
#         TreeNode left = LowestCommonAncestor(root.left, p, q);//返回的结点进行保存，可能是null
#         TreeNode right = LowestCommonAncestor(root.right, p, q);//也可能是pq，还可能是公共祖先
#         if (left != null && right != null) {
#             return root;//如果左右都存在，就说明pq都出现了，这就是，公共祖先，此时不用考虑公共祖先是自己的情况，因为上面已经做过判断了。
#         } else if (left != null) {//否则我们返回已经找到的那个值（存储在left，与right中），p或者q
#             return left;//还有一种可能就是，由下面返回的公共祖先，并将这个值一路返回到最表层
#         } else if (right != null) {
#             return right;
#         }
#         return null;
#     }
# }




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return root
        if root == p or root == q:
            return root
        left  = self.lowestCommonAncestor(root.left,  p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root
        if left is not None:
            return left
        if right is not None:
            return right
        return None


#         return self._find(root, p, q)
        
#     def _find(self, root, p, q):
#         """找到p或q或最近公共祖先"""
#         if root == None or root.val == q.val or root.val == p.val:
#             return root
        
#         left  = self._find(root.left,  p, q)
#         right = self._find(root.right, p, q)
#         return left if not right else (right if not left else root)