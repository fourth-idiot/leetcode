class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        secondLast, last = 0, 0
        for i in range(2, len(cost) + 1):
            current = min(
                secondLast + cost[i-2],
                last + cost[i-1]
            )
            secondLast = last
            last = current
        return last