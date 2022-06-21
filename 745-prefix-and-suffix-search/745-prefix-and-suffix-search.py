class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.idxs = set()
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, idx):
        current = self.root
        for c in word:
            if(c not in current.childrens):
                current.childrens[c] = TrieNode()
            current = current.childrens[c]
            current.idxs.add(idx)
            
    def search(self, word):
        current = self.root
        for c in word:
            if(c not in current.childrens):
                return -1
            current = current.childrens[c]
        return max(current.idxs)

class WordFilter:
    def __init__(self, words: List[str]):
        self.cache = {}
        self.t = Trie()
        for idx, word in enumerate(words):
            for i in range(len(word) + 1):
                wordToInsert = word[i:] + "#" + word
                self.t.insert(wordToInsert, idx)

    def f(self, prefix: str, suffix: str) -> int:
        wordToFind = suffix + "#" + prefix
        if(wordToFind not in self.cache):
            self.cache[wordToFind] = self.t.search(wordToFind)
        return self.cache[wordToFind]

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)