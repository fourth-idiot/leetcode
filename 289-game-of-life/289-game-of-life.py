class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        numRows, numCols = len(board), len(board[0])
        modifiedBoard = [[0 for _ in range(numCols)] for _ in range(numRows)]
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(numRows):
            for j in range(numCols):
                numLiveCells = 0
                for diffI, diffJ in directions:
                    neighI = i + diffI
                    neighJ = j + diffJ
                    if((neighI < 0) or (neighI >= numRows) or
                       (neighJ < 0) or (neighJ >= numCols) or
                       (board[neighI][neighJ] == 0)):
                        continue
                    else:
                        numLiveCells += 1
                if(((board[i][j] == 0) and (numLiveCells == 3)) or
                   ((board[i][j] == 1) and ((numLiveCells == 2) or (numLiveCells == 3)))):
                    modifiedBoard[i][j] = 1
        for i in range(numRows):
            for j in range(numCols):
                board[i][j] = modifiedBoard[i][j]
        return
        print(modifiedBoard)