class Solution:
    def isValidSubstring(self, l, maxFreq, k):
        return (l - maxFreq) <= k 
        
    def getMaxFreq(self, counter):
        output = 0
        for value in counter.values():
            output = max(output, value)
        return output
    
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxLen = float("-inf")
        i, j = 0, 0
        counter = {}
        while(j < n):
            counter[s[j]] = counter.get(s[j], 0) + 1
            l = (j - i + 1)
            maxFreq = self.getMaxFreq(counter)
            isValid = self.isValidSubstring(l, maxFreq, k)
            if(self.isValidSubstring(l, maxFreq, k)):
                maxLen = max(l, maxLen)
            else:
                while(not self.isValidSubstring(j-i+1, maxFreq, k)):
                    counter[s[i]] -= 1
                    i += 1
            j += 1
        return maxLen