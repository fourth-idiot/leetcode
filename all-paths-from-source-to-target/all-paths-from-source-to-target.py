class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        allPaths = []
        src, dst = 0, len(graph) - 1
        stack = [[src, neigh] for neigh in graph[src]]
        visited = {src}
        while(stack):
            path = stack.pop()
            if(path[-1] == dst):
                allPaths.append(path)
            visited.add(path[-1])
            for neigh in graph[path[-1]]:
                stack.append(path + [neigh])
            visited.remove(path[-1])
        return allPaths