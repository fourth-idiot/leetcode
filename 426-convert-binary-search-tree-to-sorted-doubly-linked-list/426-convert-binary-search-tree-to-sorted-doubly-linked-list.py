"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if(root is None): return None
        preHead = Node(-1)
        existingNode = preHead
        def helper(root):
            nonlocal existingNode
            if(root is not None):
                helper(root.left)
                newNode = Node(root.val)
                newNode.left = existingNode
                existingNode.right = newNode
                existingNode = existingNode.right
                preHead.left = newNode
                helper(root.right)
        helper(root)
        preHead.right.left = preHead.left
        preHead.left.right = preHead.right
        return preHead.right