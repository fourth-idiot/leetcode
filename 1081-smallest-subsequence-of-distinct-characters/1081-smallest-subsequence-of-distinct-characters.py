class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Approach 1
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        pos = 0
        for i in range(len(s)):
            if(s[i] < s[pos]):
                pos = i
            counter[s[i]] -= 1
            if(counter[s[i]] == 0):
                break
        newS = s[pos:].replace(s[pos], "")
        if(newS):
            return s[pos] + self.smallestSubsequence(newS)
        else:
            return s[pos]