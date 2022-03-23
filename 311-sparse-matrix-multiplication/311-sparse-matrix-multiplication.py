class Solution:
    def compressRowWise(self, mat):
        numRows, numCols = len(mat), len(mat[0])
        v = []
        rowIndex = [0]
        colIndex = []
        for i in range(numRows):
            for j in range(numCols):
                if(mat[i][j]):
                    v.append(mat[i][j])
                    colIndex.append(j)
            rowIndex.append(len(v))
        return v, rowIndex, colIndex

    def compressColumnWise(self, mat):
        numRows, numCols = len(mat), len(mat[0])
        v = []
        rowIndex = []
        colIndex = [0]
        for j in range(numCols):
            for i in range(numRows):
                if(mat[i][j]):
                    v.append(mat[i][j])
                    rowIndex.append(i)
            colIndex.append(len(v))
        return v, rowIndex, colIndex
    
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        mat1V, mat1RowIndex, mat1ColIndex = self.compressRowWise(mat1)
        mat2V, mat2RowIndex, mat2ColIndex = self.compressColumnWise(mat2)
        numRows, numCols = len(mat1), len(mat2[0])
        ans = [[0 for _ in range(numCols)] for _ in range(numRows)]
        for i in range(numRows):
            for j in range(numCols):
                rowStart = mat1RowIndex[i]
                rowEnd = mat1RowIndex[i+1]
                colStart = mat2ColIndex[j]
                colEnd = mat2ColIndex[j+1]
                while((rowStart < rowEnd) and (colStart < colEnd)):
                    if(mat1ColIndex[rowStart] < mat2RowIndex[colStart]):
                        rowStart += 1
                    elif(mat1ColIndex[rowStart] > mat2RowIndex[colStart]):
                        colStart += 1
                    else:
                        ans[i][j] += (mat1V[rowStart] * mat2V[colStart])
                        rowStart += 1
                        colStart += 1
        return ans