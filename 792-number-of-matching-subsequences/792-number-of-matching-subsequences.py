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
            current.val = current.val or val
    
    def searchPrefix(self, word):
        # Returns if the word has been queried previously and the query results
        # If the word is present in Trie, it means it was queried before
        # Previous querying results can be extrated from the val attribute of the last node.
        current = self.root
        for c in word:
            if(c not in current.childrens):
                return False, False
            current = current.childrens[c]
        return True, current.val
        
class Solution:
    def isMatchingSubseq(self, s1, s2):
        # Checks if s2 is a subsequence of s1
        # To do that, initialize pointers at the start of s1 and s2
        # If character match, then increment both the pointer by 1 step,
        # Else move the pointer on s1 by 1 step.
        # If we reach end of s2, then s2 is a subsequence of s1
        i, j = 0, 0
        while((i < len(s1)) and (j < len(s2))):
            if(s1[i] == s2[j]):
                j += 1
            i += 1
        return j == len(s2)
        
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # For every word, we can check if it is subsequence of s using isMatchingSubseq method.
        # To optimize further, we can store all the query words in a Trie
        # along with its result of whether it was subsequence of s or not.
        count = 0
        trie = Trie()
        for word in words:
            if(len(word) > len(s)):
                continue
            status, val = trie.searchPrefix(word)
            if(not status):
                val = self.isMatchingSubseq(s, word)
                trie.insert(word, val)
            count += val
        return count