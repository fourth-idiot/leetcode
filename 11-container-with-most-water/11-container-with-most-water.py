class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = float("-inf")
        i, j = 0, len(height) - 1
        while(i < j):
            if(height[i] < height[j]):
                area = (j - i) * height[i]
                maxArea = max(maxArea, area)
                i += 1
            else:
                area = (j - i) * height[j]
                maxArea = max(maxArea, area)
                j -= 1
        return maxArea
            