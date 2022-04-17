# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.modifiedRoot = None
        def helper(root):
            if(root is not None):
                helper(root.right)
                root.right = self.modifiedRoot
                self.modifiedRoot = root
                helper(root.left)
                root.left = None
        helper(root)
        return self.modifiedRoot