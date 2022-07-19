class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for i in range(1, numRows):
            current = [1]
            for j in range(1, len(output[-1])):
                current.append(output[-1][j - 1] + output[-1][j])
            current.append(1)
            output.append(current)
        return output