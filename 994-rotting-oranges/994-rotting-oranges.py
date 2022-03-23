class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:                
        numRows, numCols = len(grid), len(grid[0])
        totalSteps = [[0 for _ in range(numCols)] for _ in range(numRows)]
        queue = []
        for i in range(numRows):
            for j in range(numCols):
                if(grid[i][j] == 2):
                    grid[i][j] = 0
                    queue.append((i, j))
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        while(queue):
            row, col = queue.pop(0)
            for d in directions:
                newRow = row + d[0]
                newCol = col + d[1]
                if((newRow >= 0) and (newRow < numRows) and
                   (newCol >= 0) and (newCol < numCols) and
                   (grid[newRow][newCol] == 1)):
                    totalSteps[newRow][newCol] = totalSteps[row][col] + 1
                    grid[newRow][newCol] = 0
                    queue.append((newRow, newCol))
        output = 0
        for i in range(numRows):
            for j in range(numCols):
                output = max(totalSteps[i][j], output)
                if(grid[i][j] != 0):
                    return -1
        return output