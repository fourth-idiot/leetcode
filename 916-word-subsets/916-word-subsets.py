class Solution:
#     # Approach 1
#     def isSubset(self, word1, word2):
#         word1Counter = {}
#         for c in word1:
#             word1Counter[c] = word1Counter.get(c, 0) + 1
#         for c in word2:
#             if(c not in word1Counter):
#                 return False
#             word1Counter[c] -= 1
#             if(word1Counter[c] == 0):
#                 del word1Counter[c]
#         return True
    
#     def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
#         output = []
#         for w1 in words1:
#             flag = True
#             for w2 in words2:
#                 if(not self.isSubset(w1, w2)):
#                     flag = False
#                     break
#             if(flag):
#                 output.append(w1)
#         return output

    # Approach 
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2Counter = {}
        for word in words2:
            wordCounter = {}
            for c in word:
                wordCounter[c] = wordCounter.get(c, 0) + 1
            for c in wordCounter:
                words2Counter[c] = max(words2Counter.get(c, 0), wordCounter[c])
        output = []
        for word in words1:
            flag = True
            wordCounter = {}
            for c in word:
                wordCounter[c] = wordCounter.get(c, 0) + 1
            for c in words2Counter:
                if(wordCounter.get(c, 0) < words2Counter[c]):
                    flag = False
                    break
            if(flag):
                output.append(word)
        return output