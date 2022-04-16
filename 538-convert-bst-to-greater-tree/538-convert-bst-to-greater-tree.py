# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = 0
        def helper(root):
            nonlocal s
            if(root is None): return
            helper(root.right)
            root.val += s
            s = root.val
            helper(root.left)
        helper(root)
        return root