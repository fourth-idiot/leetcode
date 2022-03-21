class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        output = []
        start, allChars, finishedChars = 0, set(), set()
        for i, c in enumerate(s):
            if(c not in allChars):
                allChars.add(c)
            if(i == last[c]):
                finishedChars.add(c)
            if(len(allChars) == len(finishedChars)):
                output.append(i - start + 1)
                start, allChars, finishedChars = i + 1, set(), set()
        return output