# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder Traversal: Root -> Left -> Right
        # Inorder Traversal: Left -> Root -> Right
        # Hence, at any step, first value in the preorder traversal represents
        # root of the binary tree at that point.
        # If that value is at the i'th index in inorder list,
        # then all the values to its left are part of left subtree.
        # Similarly, all the values to its right are part of the right subtree.
        if(len(inorder) == 0):
            return None
        val = preorder.pop(0)
        node = TreeNode(val)
        idx = inorder.index(val)
        leftInorder = inorder[:idx]
        rightInorder = inorder[(idx + 1):]
        # Since we traverse left node before right node in preorder tranversal,
        # node.left needs to be evaluated before node.right
        node.left = self.buildTree(preorder, leftInorder)
        node.right = self.buildTree(preorder, rightInorder)
        return node