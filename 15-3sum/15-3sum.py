class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(k, target):
            i, j = k + 1, n - 1
            pairs = []
            while(i < j):
                if((nums[i] + nums[j]) < target):
                    i += 1
                elif((nums[i] + nums[j]) == target):
                    pairs.append([nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while((i < j) and (nums[i-1] == nums[i])):
                        i += 1
                else:
                    j -= 1
            return pairs
        
        nums.sort()
        n = len(nums)
        output = []
        for i in range(n):
            if(nums[i] > 0):
                return output
            if((i == 0) or (nums[i-1] != nums[i])):
                pairs = twoSum(i, -nums[i])
                for pair in pairs:
                    output.append(pair + [nums[i]])
        return output