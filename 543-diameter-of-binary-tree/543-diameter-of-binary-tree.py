# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if(root is None):
                return 0, 0
            else:
                leftDepth, leftDiameter = helper(root.left)
                rightDepth, rightDiameter = helper(root.right)
                return (1 + max(leftDepth, rightDepth), max(leftDiameter, rightDiameter, 1 + leftDepth + rightDepth))
        return helper(root)[1] - 1