class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        numRows, numCols = len(image), len(image[0])
        def helper(i, j, refColor):
            if((i < 0) or
               (i >= numRows) or
               (j < 0) or
               (j >= numCols) or
               (image[i][j] != refColor)):
                return
            image[i][j] = color
            helper(i, j - 1, refColor)
            helper(i, j + 1, refColor)
            helper(i - 1, j, refColor)
            helper(i + 1, j, refColor)
        if(image[sr][sc] != color): helper(sr, sc, image[sr][sc])
        return image