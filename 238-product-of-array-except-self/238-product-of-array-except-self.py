class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lProd = [1 for _ in range(n)]
        rProd = [1 for _ in range(n)]
        for i in range(n):
            if(i != 0):
                lProd[i] = lProd[i-1] * nums[i-1]
                rProd[(n-1)-i] = rProd[((n-1)-i)+1] * nums[((n-1)-i)+1]
        prod = [(lProd[i] * rProd[i]) for i in range(n)]
        return prod