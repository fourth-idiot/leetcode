class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Create adjacency list representation of the graph
        adjList = {}
        for edge in edges:
            node1, node2 = edge
            if(node1 in adjList):
                adjList[node1].append(node2)
            else:
                adjList[node1] = [node2]
            if(node2 in adjList):
                adjList[node2].append(node1)
            else:
                adjList[node2] = [node1]
        
        # # Run DFS
        # visited = set()
        # stack = [source]
        # while(stack):
        #     node = stack.pop()
        #     if(node == destination):
        #         return True
        #     visited.add(node)
        #     for neigh in adjList[node]:
        #         if(neigh not in visited):
        #             stack.append(neigh)
        # return False
        
        # Run BFS
        visited = set()
        queue = [source]
        while(queue):
            node = queue.pop(0)
            if(node == destination):
                return True
            visited.add(node)
            for neigh in adjList[node]:
                if(neigh not in visited):
                    queue.append(neigh)
        return False