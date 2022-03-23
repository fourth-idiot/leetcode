class Solution:        
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        src = (0, 0)
        dst = (n - 1, n - 1)
        if((grid[src[0]][src[1]] != 0) or (grid[dst[0]][dst[1]] != 0)):
            return -1
        directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        queue = [src]
        grid[0][0] = 1
        while(queue):
            row, col = queue.pop(0)
            distance = grid[row][col]
            if((row == dst[0]) and (col == dst[1])):
                return distance
            for d in directions:
                newRow = row + d[0]
                newCol = col + d[1]
                if((newRow >= 0) and (newRow < n) and
                   (newCol >= 0) and (newCol < n) and
                   (grid[newRow][newCol] == 0)):
                    grid[newRow][newCol] = distance + 1
                    queue.append((newRow, newCol))
        return -1