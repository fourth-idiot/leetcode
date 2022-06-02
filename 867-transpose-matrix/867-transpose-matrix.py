class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        numRows, numCols = len(matrix), len(matrix[0])
        matrixT = [[0 for _ in range(numRows)] for _ in range(numCols)]
        for i in range(numRows):
            for j in range(numCols):
                matrixT[j][i] = matrix[i][j]
        return matrixT