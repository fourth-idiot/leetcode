class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def dfs(i, j, remainingMoves):
            # Similar to the number of islands problem, here we can start DFS from (startRow, startColumn).
            # Now, we need to check for three conditions:
            # 1. If we are out of moves and we are still inside the bounds, then no paths are possible. Hence we return 0.
            # 2. Else if we are out of bounds, then this is one possible path. Hence we return 1.
            # 3. Else, we need to take sum of all possible paths by moving in four directions with one less move.
            isOutOfBound = (i < 0) or (i >= m) or (j < 0) or (j >= n)
            if((remainingMoves == 0) and (not isOutOfBound)):
                return 0
            elif(isOutOfBound):
                return 1
            else:
                return (dfs(i - 1, j, remainingMoves - 1) + \
                       dfs(i + 1, j, remainingMoves - 1) + \
                       dfs(i, j - 1, remainingMoves - 1) + \
                       dfs(i, j + 1, remainingMoves - 1)) % (7 + (10 ** 9))
        return dfs(startRow, startColumn, maxMove)