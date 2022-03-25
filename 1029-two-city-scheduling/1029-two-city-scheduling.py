class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key=lambda cost: cost[0] - cost[1])
        minCost = 0
        for i in range(n // 2):
            minCost += (costs[i][0] + costs[n-i-1][1])
        return minCost