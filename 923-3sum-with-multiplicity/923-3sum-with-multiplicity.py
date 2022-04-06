class Solution:
    def twoSumMulti(self, arr, i, target):
        count = 0
        freq = {}
        for num in arr[i+1:]:
            remaining = target - num
            if(remaining in freq):
                count += freq[remaining]
            freq[num] = freq.get(num, 0) + 1
        return count
    
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = 0
        for i in range(len(arr)):
            count += self.twoSumMulti(arr, i, target - arr[i])
        return count % (10 ** 9 + 7)