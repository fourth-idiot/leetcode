# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEqual(self, p, q):
        if((not p) and (not q)):
            return True
        elif(((not p) and (q)) or
             ((not q) and (p))):
            return False
        elif(p.val != q.val):
            return False
        else:
            return ((self.isEqual(p.left, q.left)) and
                    (self.isEqual(p.right, q.right)))
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(root):
            if(root is None):
                return
            if self.isEqual(root,subRoot):
                return True
                # return self.isEqual(root, subRoot)
            else:
                return (helper(root.left) or helper(root.right))
        return helper(root)