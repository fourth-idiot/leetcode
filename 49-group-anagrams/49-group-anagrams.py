class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        sortedWordIndexMap = {}
        for s in strs:
            sortedS = "".join(sorted(s))
            if(sortedS in sortedWordIndexMap):
                output[sortedWordIndexMap[sortedS]].append(s)
            else:
                sortedWordIndexMap[sortedS] = len(output)
                output.append([s])
        return output