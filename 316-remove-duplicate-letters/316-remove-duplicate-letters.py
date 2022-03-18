class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        pos = 0
        for i in range(len(s)):
            if(s[i] < s[pos]):
                print(s[i], s[pos])
                pos = i
            counter[s[i]] -= 1
            if(counter[s[i]] == 0):
                break
        newS = s[pos:].replace(s[pos], "")
        if(newS):
            return s[pos] + self.removeDuplicateLetters(newS)
        else:
            return s[pos]