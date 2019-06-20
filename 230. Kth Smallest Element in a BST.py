# day 41 2019-06-19 Wed
# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = []
        self.getSmallest(root, ans)
        return ans[k-1]
    def getSmallest(self, root, ret):
        if root:
            # if len(ret) == k:
            #     return ret[-1]
            self.getSmallest(root.left,ret)
            ret.append(root.val)
            self.getSmallest(root.right,ret)



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def insert(self, x):
        if self.val:
            if x < self.val:
                if self.left == None:
                    self.left = TreeNode(x)
                else:
                    self.left.insert(x)
            else:
                if self.right == None:
                    self.right = TreeNode(x)
                else:
                    self.right.insert(x)
        else:
            self.val = x

if __name__ == "__main__":
    root = [3,1,4,1,2]
    r = TreeNode(root[0])
    r.insert(1)
    for i in root:
        r.insert(i)
