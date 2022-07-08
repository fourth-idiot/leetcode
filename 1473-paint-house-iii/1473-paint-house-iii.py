class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def helper(startIdx, endIdx, color, remainingTarget):
            if(remainingTarget < 0):
                return float("inf")
            
            costOfNeighborhood = 0
            for i in range(startIdx, endIdx + 1):
                # If house from the neighborhood is already colored with
                # a color which does not match with our selection
                if((houses[i]) and (houses[i] != color)):
                    return float("inf")
                elif(houses[i] == 0):
                    costOfNeighborhood += cost[i][color - 1]
            
            newStartIdx = endIdx + 1
            if(newStartIdx == len(houses)):
                return costOfNeighborhood
            
            minCostOfRemainingCity = float("inf")
            for newEndIdx in range(newStartIdx, len(houses) - (remainingTarget - 1)):
                for newColor in range(1, n + 1):
                    if(newColor == color):
                        continue
                    costOfRemainingCity = helper(newStartIdx, newEndIdx, newColor, remainingTarget - 1)
                    if costOfRemainingCity < minCostOfRemainingCity:
                        minCostOfRemainingCity = costOfRemainingCity
            return costOfNeighborhood + minCostOfRemainingCity
        
        minCostToPaint = float("inf")
        # Loop over all possible ranges of forming a neighborhood starting from 0'th index house
        for endIdx in range(len(houses) - (target - 1)):
            # Loop over all possible color options
            for color in range(1, n + 1):
                costToPaint = helper(0, endIdx, color, target - 1)
                if(costToPaint < minCostToPaint):
                    minCostToPaint = costToPaint
                
        return -1 if (minCostToPaint == float("inf")) else minCostToPaint