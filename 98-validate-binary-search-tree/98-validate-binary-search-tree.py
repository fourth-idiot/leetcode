# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, lower, upper):
            if(root is None):
                return True
            else:
                isInRange = ((root.val > lower) and (root.val < upper))
                return (isInRange and
                        helper(root.left, lower, root.val) and
                        helper(root.right, root.val, upper))
        return helper(root, float("-inf"), float("inf"))