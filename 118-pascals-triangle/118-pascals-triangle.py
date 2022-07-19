class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(1, numRows + 1):
            current = []
            for j in range(i):
                if((j == 0) or (j == (i - 1))):
                    current.append(1)
                else:
                    current.append(output[-1][j - 1] + output[-1][j])
            output.append(current)
        return output