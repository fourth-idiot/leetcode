"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        # Find the root node
        root = node
        while(root.parent):
            root = root.parent
        
        # Inorder tranversal of the BST
        nodes = []
        def helper(root):
            if(root.left is not None):
                helper(root.left)
            nodes.append(root)
            if(root.right is not None):
                helper(root.right)
        helper(root)
        
        # Look for the given node in inorder traversal,
        # and return the next node
        for i in range(len(nodes)):
            if(nodes[i] == node):
                if((i + 1) == len(nodes)):
                    return None
                return nodes[i + 1]