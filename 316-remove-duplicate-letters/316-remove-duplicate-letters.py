class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # # Approach 1
        # counter = {}
        # for c in s:
        #     counter[c] = counter.get(c, 0) + 1
        # pos = 0
        # for i in range(len(s)):
        #     if(s[i] < s[pos]):
        #         pos = i
        #     counter[s[i]] -= 1
        #     if(counter[s[i]] == 0):
        #         break
        # newS = s[pos:].replace(s[pos], "")
        # if(newS):
        #     return s[pos] + self.removeDuplicateLetters(newS)
        # else:
        #     return s[pos]
        
        # Approach 2
        stack = []
        seen = set()
        last_occurence = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if(c not in seen):
                while((stack) and (c < stack[-1]) and (i < last_occurence[stack[-1]])):
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return "".join(stack)