class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # For a matrix of dimensions m * n, initialize its transpose having shape n * m
        # with zero values. Loop over all the elements from the original matrix
        # and put the element from i'th row and j'th column at j'th row and i'th column
        # in its transpose.
        # Time Complexity: O(n^2)
        # Space Complexity: O(n ^ 2)
        numRows, numCols = len(matrix), len(matrix[0])
        matrixT = [[0 for _ in range(numRows)] for _ in range(numCols)]
        for i in range(numRows):
            for j in range(numCols):
                matrixT[j][i] = matrix[i][j]
        return matrixT