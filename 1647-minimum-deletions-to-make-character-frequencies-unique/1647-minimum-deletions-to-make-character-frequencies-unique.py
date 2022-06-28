class Solution:
    def minDeletions(self, s: str) -> int:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        values = [counter[c] for c in counter]
        values.sort(reverse=True)
        prevVal, output = float("inf"), 0
        for val in values:
            if(prevVal == 0):
                output += val
            elif(val >= prevVal):
                output += (val - (prevVal - 1))
                prevVal -= 1
            else:
                prevVal = val
        return output