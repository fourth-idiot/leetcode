class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Approach 1
        n = query_row + 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        matrix[0][0] = poured
        for i in range(n):
            for j in range(0, i+1):
                if(matrix[i][j] > 1):
                    overflow = matrix[i][j] - 1
                    if((i+1) < n):
                        matrix[i+1][j] += overflow / 2
                        matrix[i+1][j+1] += overflow / 2
                    matrix[i][j] = 1
        return matrix[query_row][query_glass]