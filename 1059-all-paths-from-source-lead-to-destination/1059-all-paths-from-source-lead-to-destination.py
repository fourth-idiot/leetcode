class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node):
            if(node in visited):
                return False
            visited.add(node)
            if(node not in adjList):
                output = node == destination
            else:
                output = True
                for neigh in adjList[node]:
                    output = output and dfs(neigh)
            visited.remove(node)
            return output
        
        adjList = {}
        for src, dst in edges:
            if(src not in adjList):
                adjList[src] = []
            adjList[src].append(dst)
        visited = set()
        return dfs(source)