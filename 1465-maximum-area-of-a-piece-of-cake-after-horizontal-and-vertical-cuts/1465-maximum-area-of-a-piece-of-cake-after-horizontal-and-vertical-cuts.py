class Solution:
    def getSides(self, n: int, cuts):
        cuts.extend([0, n])
        cuts.sort()
        sides = [(cuts[i] - cuts[i - 1]) for i in range(1, len(cuts))]
        sides.sort(reverse=True)
        return sides
        
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalSides = self.getSides(h, horizontalCuts)
        verticalSides = self.getSides(w, verticalCuts)
        return (horizontalSides[0] * verticalSides[0]) % (7 + (10 ** 9))