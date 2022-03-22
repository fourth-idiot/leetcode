"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        def dfs(node):
            if(node in oldToNew):
                return oldToNew[node]
            newNode = Node(node.val)
            oldToNew[node] = newNode
            for neigh in node.neighbors:
                newNode.neighbors.append(dfs(neigh))
            return newNode
        if(node is None):
            return None
        return dfs(node)    