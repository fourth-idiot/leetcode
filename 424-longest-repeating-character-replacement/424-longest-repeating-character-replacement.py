class Solution:
    def isValidSubstring(self, l, maxFreq, k):
        """Checks if the substring is valid according to the problem statement."""
        return (l - maxFreq) <= k
        
    def getMaxFreq(self, counter):
        """Get frequency of the most frequent character in a string."""
        maxFreq = 0
        for freq in counter.values():
            maxFreq = max(maxFreq, freq)
        return maxFreq
    
    def characterReplacement(self, s: str, k: int) -> int:
        maxL = float("-inf")
        counter = {}
        i, j = 0, 0
        while(j < len(s)):
            counter[s[j]] = counter.get(s[j], 0) + 1
            maxFreq = self.getMaxFreq(counter)
            l = (j - i + 1)
            isValid = self.isValidSubstring(l, maxFreq, k)
            if(self.isValidSubstring(l, maxFreq, k)):
                maxL = max(l, maxL)
            else:
                while(not self.isValidSubstring(l, maxFreq, k)):
                    counter[s[i]] -= 1
                    maxFreq = self.getMaxFreq(counter)
                    i += 1
                    l = (j - i + 1)
            j += 1
        return maxL