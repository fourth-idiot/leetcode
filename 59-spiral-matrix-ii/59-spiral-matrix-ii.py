class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0 for _ in range(n)] for _ in range(n)]
        currentI, currentJ = 0, 0
        direction = "right"
        for num in range(1, n * n + 1):
            grid[currentI][currentJ] = num
            if(direction == "right"):
                nextI = currentI
                nextJ = currentJ + 1
                if((nextJ == n) or (grid[nextI][nextJ] != 0)):
                    direction = "down"
                    nextI = currentI + 1
                    nextJ = currentJ
            elif(direction == "down"):
                nextI = currentI + 1
                nextJ = currentJ
                if((nextI == n) or (grid[nextI][nextJ] != 0)):
                    direction = "left"
                    nextI = currentI
                    nextJ = currentJ - 1    
            elif(direction == "left"):
                nextI = currentI
                nextJ = currentJ - 1
                if((nextJ < 0) or (grid[nextI][nextJ] != 0)):
                    direction = "up"
                    nextI = currentI - 1
                    nextJ = currentJ    
            elif(direction == "up"):
                nextI = currentI - 1
                nextJ = currentJ
                if((nextI < 0) or (grid[nextI][nextJ] != 0)):
                    direction = "right"
                    nextI = currentI
                    nextJ = currentJ + 1    
            else:
                print("[ERROR] Unknown direction")
                return
            currentI = nextI
            currentJ = nextJ
        return grid