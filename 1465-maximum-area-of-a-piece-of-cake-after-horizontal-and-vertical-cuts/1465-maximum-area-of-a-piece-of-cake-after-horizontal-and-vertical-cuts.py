class Solution:
    def getSides(self, n: int, cuts: List[int]) -> List[int]:
        # Given the total length and an array of cuts on it,
        # it returns an array of side of rectangles formed by those cuts in descending order.
        # As the first step, we arrange all the cuts in  increasing order of their distances from one end.
        # Then, we can find the side of rectangle formed by i'th and (i - 1)'th cut using (cuts[i] - cuts[i - 1]).
        # Finally, we sort the array of sides in descending order as we need that rectangle with maximum area
        cuts.extend([0, n])
        cuts.sort()
        sides = [(cuts[i] - cuts[i - 1]) for i in range(1, len(cuts))]
        sides.sort(reverse=True)
        return sides
        
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Find the length and breadth of all rectangles formed by the cuts
        horizontalSides = self.getSides(h, horizontalCuts)
        verticalSides = self.getSides(w, verticalCuts)
        # Find the area by taking the longest length and width
        return (horizontalSides[0] * verticalSides[0]) % (7 + (10 ** 9))