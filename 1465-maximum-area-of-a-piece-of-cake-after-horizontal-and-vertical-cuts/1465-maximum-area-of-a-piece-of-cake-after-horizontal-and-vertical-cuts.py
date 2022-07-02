class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0, h])
        horizontalCuts.sort()
        horizontalCutsDiff = [(horizontalCuts[i] - horizontalCuts[i - 1]) for i in range(1, len(horizontalCuts))]
        horizontalCutsDiff.sort(reverse=True)
        
        verticalCuts.extend([0, w])
        verticalCuts.sort()
        verticalCutsDiff = [(verticalCuts[i] - verticalCuts[i - 1]) for i in range(1, len(verticalCuts))]
        verticalCutsDiff.sort(reverse=True)
        
        return (horizontalCutsDiff[0] * verticalCutsDiff[0]) % (7 + (10 ** 9))
        