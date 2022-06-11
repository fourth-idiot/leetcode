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
        # print(leftSum, rightSum)
        minOp = float("inf")
        for val in leftSum:
            remainingX = x - val
            if(remainingX in rightSum):
                op = leftSum[val] + rightSum[remainingX]
                if(op <= n):
                    minOp = min(minOp, op)
        if(minOp == float("inf")): return -1
        else: return minOp
            
#         print(leftSum)
#         print(rightSum)
# #         1, 2, 6, 8, 11
# #         11, 10, 9, 5, 3
        
        
# #         a = 0, 3, 5, 25, 26, 27, 30
# #         b = 30, 27, 25, 5, 4, 3, 0
        
# #         4, 2 20, 1, 1, 3
# #         0, 4, ...
# #         31, 27, 25, 5, 4, 3, 0
        
# #         a[i] + b[j] = target such that i + j is minimum
        
        