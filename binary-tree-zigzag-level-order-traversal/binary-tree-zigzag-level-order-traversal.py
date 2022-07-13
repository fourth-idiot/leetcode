# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root is None):
            return root
        allNodes = []
        queue = [root]
        isReverse = False
        while(queue):
            levelNodes = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                levelNodes.append(node.val)
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            if(isReverse):
                allNodes.append(levelNodes[::-1])
            else:
                allNodes.append(levelNodes)
            isReverse = not isReverse
        return allNodes