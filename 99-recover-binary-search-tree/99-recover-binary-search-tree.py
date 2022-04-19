# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        output = []
        def helper(root):
            if(root is not None):
                helper(root.left)
                output.append(root)
                helper(root.right)
        helper(root)
        node1, node2 = None, None
        for i in range(len(output) - 1):
            if(output[i].val > output[i + 1].val):
                node2 = output[i + 1]
                if(node1 is None):
                    node1 = output[i]    
        node1.val, node2.val = node2.val, node1.val
        return root