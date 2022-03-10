class UnionFind:
    def __init__(self, n):
        self.numConnectedComponents = n
        self.root = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        
    def Union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if(root1 != root2):
            if(self.rank[root1] > self.rank[root2]):
                self.root[root2] = root1
            elif(self.rank[root2] > self.rank[root1]):
                self.root[root1] = root2
            else:
                self.root[root2] = root1
                self.rank[root1] += 1
            self.numConnectedComponents -= 1
    
    def find(self, node):
        if(node == self.root[node]):
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(len(edges) != (n-1)):
            return False
        uf = UnionFind(n)
        for edge in edges:
            uf.Union(edge[0], edge[1])
        return (uf.numConnectedComponents == 1)
        