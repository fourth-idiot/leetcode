"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}
        def dfs(node):
            if(node is None):
                return None
            elif(node in oldToNew):
                return oldToNew[node]
            else:
                newNode = Node(node.val)
                oldToNew[node] = newNode
                newNode.next = dfs(node.next)
                newNode.random = dfs(node.random)
            return newNode
        return dfs(head)