"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        output = []
        if(root is None):
            return output
        queue = [root]
        prevNumNodes = 1
        while(queue):
            prevNodes = []
            currentNumNodes = 0
            for _ in range(prevNumNodes):
                node = queue.pop(0)
                prevNodes.append(node.val)
                for neigh in node.children:
                    queue.append(neigh)
                    currentNumNodes += 1
            output.append(prevNodes)
            prevNumNodes = currentNumNodes
        return output