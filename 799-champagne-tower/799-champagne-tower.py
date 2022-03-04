class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
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