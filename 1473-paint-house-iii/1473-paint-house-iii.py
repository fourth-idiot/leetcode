class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # If we think about it in a dynamic programming way,
        # we can color a neighborhood from `startIdx` to `endIdx` with `color` (Cost: x).
        # Now, we can color rest of the city starting from `endIdx + 1` with `target - 1` neighborhoods,
        # such that previous color is not used for the first neighborhood of the remaining part (Cost of all each of those possibilities: y)
        # Then, minimum cost of painting will be x + min (y)
        # i.e. We need 4 variable (startIdx, endIdx, color, remainingTarget) to define one sub problem.
        
        @cache
        def helper(startIdx, endIdx, color, remainingTarget):
            # Not possible to paint if we exceed the given number of neighborhoods
            if(remainingTarget < 0):
                return float("inf")
            
            # Find cost of painting neighborhood from `startIdx` to `endIdx` with `color`
            costOfNeighborhood = 0
            for i in range(startIdx, endIdx + 1):
                # Not possible to paint if the house is already colored with
                # a color different than the selected `color`
                if((houses[i]) and (houses[i] != color)):
                    return float("inf")
                elif(houses[i] == 0):
                    costOfNeighborhood += cost[i][color - 1]
            
            # Loop over all possibilities for the rest of the city
            newStartIdx = endIdx + 1
            if(newStartIdx == len(houses)):
                return costOfNeighborhood
            
            minCostOfRemainingCity = float("inf")
            for newEndIdx in range(newStartIdx, len(houses) - (remainingTarget - 1)):
                for newColor in range(1, n + 1):
                    # Skip coloring the adjacent neighborhoods with the same color
                    if(newColor == color):
                        continue
                    costOfRemainingCity = helper(newStartIdx, newEndIdx, newColor, remainingTarget - 1)
                    if costOfRemainingCity < minCostOfRemainingCity:
                        minCostOfRemainingCity = costOfRemainingCity
            return costOfNeighborhood + minCostOfRemainingCity
        
        
        # Loop over all possible ranges of forming a neighborhood starting from 0'th index house
        minCostToPaint = float("inf")
        for endIdx in range(len(houses) - (target - 1)):
            # Loop over all possible color options
            for color in range(1, n + 1):
                costToPaint = helper(0, endIdx, color, target - 1)
                if(costToPaint < minCostToPaint):
                    minCostToPaint = costToPaint
                    
        return -1 if (minCostToPaint == float("inf")) else minCostToPaint