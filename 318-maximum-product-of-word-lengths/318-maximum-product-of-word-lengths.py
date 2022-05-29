class Solution:
#     # Approach 1
#     def hasNoCommonLetters(self, w1, w2):
#         # Checks if the two words have any letters in common
#         # Loop over all characters from the first word
#         # For each character, check if that character is present in the second word
#         for c1 in w1:
#             if(c1 in w2):
#                 return True
#         return False
            
#     def maxProduct(self, words: List[str]) -> int:
#         # Loop over all words pairs
#         # Update the maximum product if the word pair does not have any letter in common
#         n = len(words)
#         maxProduct = 0
#         for i in range(n):
#             w1 = words[i]
#             for j in range(i + 1, n):
#                 w2 = words[j]
#                 if(not self.hasNoCommonLetters(w1, w2)):
#                     maxProduct = max(maxProduct, len(w1) * len(w2))
#         return maxProduct

    # Approach 2 (Using Bit Manipulation)
    # A string can be represented as a 26 bit number (zyxwvutsrqponmlkjihgfedcba),
    # where each bit represents the presence of the i'th character in the string
    # For example, apple can be represented as 00000000001000100000010001
    def convertToBinary(self, word):
        binaryWord = 0
        for c in word:
            binaryWord |= 1 << ord(c) - ord("a")
        return binaryWord
    
    def maxProduct(self, words):
        n = len(words)
        maxProduct = 0
        binaryWords = [0] * n
        lens = [0] * n
        for i in range(n):
            binaryWords[i] = self.convertToBinary(words[i])
            lens[i] = len(words[i])
        for i in range(n):
            bw1 = binaryWords[i]
            for j in range(i + 1, n):
                bw2 = binaryWords[j]
                if(bw1 & bw2 == 0):
                    maxProduct = max(maxProduct, lens[i] * lens[j])
        return maxProduct