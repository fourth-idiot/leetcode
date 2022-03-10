class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) < 2):
            return len(s)
        else:
            maxLen = 0
            i, j = 0, 0
            history = set()
            while(j < len(s)):
                if(s[j] in history):
                    maxLen = max((j - i), maxLen)
                    while(s[i] != s[j]):
                        history.remove(s[i])
                        i += 1
                    i += 1
                else:
                    history.add(s[j])
                j += 1
            maxLen = max((j - i), maxLen)
            return maxLen