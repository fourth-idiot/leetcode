class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # # Approach 1
        # n = query_row + 1
        # matrix = [[0 for _ in range(n)] for _ in range(n)]
        # matrix[0][0] = poured
        # for i in range(n):
        #     for j in range(0, i+1):
        #         if(matrix[i][j] > 1):
        #             overflow = matrix[i][j] - 1
        #             if((i+1) < n):
        #                 matrix[i+1][j] += overflow / 2
        #                 matrix[i+1][j+1] += overflow / 2
        #             matrix[i][j] = 1
        # return matrix[query_row][query_glass]
    
        # Approach 2 (DP Approach)
        dp = {}
        dp["0,0"] = poured
        def helper(row, col):
            if((row < 0) or (col < 0) or (col > row)):
                return 0
            key = "{},{}".format(row, col)
            if(key in dp):
                return dp[key]
            topLeft = helper(row-1, col-1)
            topRight = helper(row-1, col)
            dp[key] = (max(0, topLeft-1) + max(0, topRight-1)) / 2
            return dp[key]
        return min(1, helper(query_row, query_glass))