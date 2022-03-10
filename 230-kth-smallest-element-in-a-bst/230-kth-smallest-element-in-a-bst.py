# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     output = []
    #     def helper(root):
    #         if(root is not None):
    #             if(root.left is not None):
    #                 helper(root.left)
    #             output.append(root.val)
    #             if(root.right is not None):
    #                 helper(root.right)
    #     helper(root)
    #     return output
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None
        def helper(root):
            nonlocal count, ans
            if(root is None):
                return
            helper(root.left)
            count += 1
            if(count == k):
                ans = root.val
            helper(root.right)
        helper(root)
        return ans