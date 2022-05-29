class Solution:
    def hasNoCommonLetters(self, w1, w2):
        for c1 in w1:
            if(c1 in w2):
                return True
        return False
            
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        maxProduct = 0
        for i in range(n):
            w1 = words[i]
            for j in range(i + 1, n):
                w2 = words[j]
                if(not self.hasNoCommonLetters(w1, w2)):
                    maxProduct = max(maxProduct, len(w1) * len(w2))
        return maxProduct