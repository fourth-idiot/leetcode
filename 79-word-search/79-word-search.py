class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if(k == len(word)):
                return True
            elif(((i < 0) or (i >= numRows)) or
               ((j < 0) or (j >= numCols)) or
               ((i, j) in visited)):
                return False
            elif(board[i][j] != word[k]):
                return False
            else:
                visited.add((i, j))
                ans = (
                    dfs(i - 1, j, k + 1) or 
                    dfs(i + 1, j, k + 1) or
                    dfs(i, j - 1, k + 1) or
                    dfs(i, j + 1, k + 1)
                )
                visited.remove((i, j))
                return ans
        
        numRows, numCols = len(board), len(board[0])
        visited = set()
        for i in range(numRows):
            for j in range(numCols):
                if(dfs(i, j, 0)):
                    return True
        return False