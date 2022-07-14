# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if(root is None):
                return float("-inf"), float("-inf")
            leftEdge, leftPathSum = helper(root.left)
            rightEdge, rightPathSum = helper(root.right)
            # Find the maximum of all the possibilities
            # For the longest edge we can select,
            #   1. Root only
            #   2. Root + leftEdge
            #   3. Root + rightEdge
            # For the maximum path sum we can select,
            #   1. New longest edge
            #   2. Maximum path sum of the left subtree
            #   3. Maximum path sum of the right subtree
            #   4. Root + leftEdge + rightEdge
            newEdge = max(root.val, root.val + max(leftEdge, rightEdge))
            return (newEdge, max(newEdge, leftPathSum, rightPathSum, root.val + leftEdge + rightEdge))
        return helper(root)[1]