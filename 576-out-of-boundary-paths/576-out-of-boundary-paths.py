class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def dfs(i, j, prevNumMoves):
            isOutOfBound = (i < 0) or (i >= m) or (j < 0) or (j >= n)
            if((prevNumMoves == maxMove) and (not isOutOfBound)):
                return 0
            elif(isOutOfBound):
                return 1
            else:
                return (dfs(i - 1, j, prevNumMoves + 1) + \
                       dfs(i + 1, j, prevNumMoves + 1) + \
                       dfs(i, j - 1, prevNumMoves + 1) + \
                       dfs(i, j + 1, prevNumMoves + 1)) % (7 + (10 ** 9))
        return dfs(startRow, startColumn, 0)