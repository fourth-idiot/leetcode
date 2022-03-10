class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create adjacency matrix
        adjList = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            adjList[course].append(prerequisite)
            
        # DFS
        visited = set()
        def isCycle(prerequisite):
            if(prerequisite in visited):
                return True
            visited.add(prerequisite)
            for course in adjList[prerequisite]:
                if(isCycle(course)):
                    return True
            visited.remove(prerequisite)
            adjList[prerequisite] = []
            return False
        
        # Run DFS through graph
        # Return if any one cycle detected
        for prerequisite in adjList:
            if(isCycle(prerequisite)):
                return False
        return True