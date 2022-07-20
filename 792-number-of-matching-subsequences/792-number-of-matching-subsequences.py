class TrieNode:
    def __init__(self, val=False):
        self.val = val
        self.childrens = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode(True)
        
    def insert(self, word, val):
        current = self.root
        for c in word:
            if(c not in current.childrens):
                current.childrens[c] = TrieNode(val)
            current = current.childrens[c]
    
    def searchPrefix(self, word):
        current = self.root
        for c in word:
            if(c not in current.childrens):
                return False, False
            current = current.childrens[c]
        return True, current.val
        
class Solution:
    def isMatchingSubseq(self, s1, s2):
        i, j = 0, 0
        while((i < len(s1)) and (j < len(s2))):
            if(s1[i] == s2[j]):
                j += 1
            i += 1
        return j == len(s2)
        
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        trie = Trie()
        for word in words:
            if(len(word) > len(s)):
                continue
            status, val = trie.searchPrefix(word)
            if(status):
                count += val
            else:
                val = self.isMatchingSubseq(s, word)
                trie.insert(word, val)
                count += val
        return count