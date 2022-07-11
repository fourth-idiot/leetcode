# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(root is None):
            return []
        output = []
        queue = [root]
        currNumNodes = 1
        while(queue):
            nextNumNodes = 0
            for i in range(currNumNodes):
                node = queue.pop(0)
                if((i + 1) == currNumNodes):
                    output.append(node.val)
                if(node.left):
                    queue.append(node.left)
                    nextNumNodes += 1
                if(node.right):
                    queue.append(node.right)
                    nextNumNodes += 1
            currNumNodes = nextNumNodes
        return output