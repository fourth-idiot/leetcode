class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # # Using DFS
        # allPaths = []
        # src, dst = 0, len(graph) - 1
        # stack = [[src]]
        # visited = set()
        # while(stack):
        #     path = stack.pop()
        #     if(path[-1] == dst):
        #         allPaths.append(path)
        #     visited.add(path[-1])
        #     for neigh in graph[path[-1]]:
        #         stack.append(path + [neigh])
        #     visited.remove(path[-1])
        # return allPaths
        
        # Using BFS
        allPaths = []
        src, dst = 0, len(graph) - 1
        queue = [[src]]
        visited = set()
        while(queue):
            path = queue.pop(0)
            if(path[-1] == dst):
                allPaths.append(path)
            visited.add(path[-1])
            for neigh in graph[path[-1]]:
                queue.append(path + [neigh])
            # visited.remove(path[-1])
        return allPaths