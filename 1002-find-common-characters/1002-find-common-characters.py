class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        previous = {}
        for c in words[0]:
            previous[c] = previous.get(c, 0) + 1
        for word in words:
            current = {}
            for c in word:
                count = previous.get(c, 0)
                if(count > 0):
                    previous[c] -= 1
                    current[c] = current.get(c, 0) + 1
            previous = current
        output = [c for c in current for _ in range(current[c])]
        return output