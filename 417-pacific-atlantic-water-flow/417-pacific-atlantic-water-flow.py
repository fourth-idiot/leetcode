class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(row, col, visited, prevHeight):
            if(((row, col) in visited) or
               ((row < 0) or (row >= numRows)) or
               ((col < 0) or (col >= numCols)) or
               (heights[row][col] < prevHeight)):
                return
            visited.add((row, col))
            dfs(row, col-1, visited, heights[row][col])
            dfs(row, col+1, visited, heights[row][col])
            dfs(row-1, col, visited, heights[row][col])
            dfs(row+1, col, visited, heights[row][col])
            
        numRows, numCols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        for j in range(numCols):
            dfs(0, j, pacific, heights[0][j])
            dfs(numRows - 1, j, atlantic, heights[numRows - 1][j])
        for i in range(numRows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, numCols - 1, atlantic, heights[i][numCols - 1])
        return list(pacific.intersection(atlantic))