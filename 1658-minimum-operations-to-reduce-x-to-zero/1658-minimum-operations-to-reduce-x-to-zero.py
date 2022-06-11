class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        leftSum = [0 for _ in range(n + 1)]
        rightSum = [0 for _ in range(n + 1)]
        for i in range(n):
            leftSum[i + 1] = leftSum[i] + nums[i]
            rightSum[i + 1] = rightSum[i] + nums[n - i - 1]
        
        leftSum = {val: index for index, val in enumerate(leftSum)}
        rightSum = {val: index for index, val in enumerate(rightSum)}
        minOp = float("inf")
        for val in leftSum:
            remainingX = x - val
            if(remainingX in rightSum):
                op = leftSum[val] + rightSum[remainingX]
                if(op <= n):
                    minOp = min(minOp, op)
        if(minOp == float("inf")): return -1
        else: return minOp
        
        