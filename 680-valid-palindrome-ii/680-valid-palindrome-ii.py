class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while(i < j):
            if(s[i] != s[j]):
                return False
            else:
                i += 1
                j -= 1
        return True
        
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while(i < j):
            if(s[i] != s[j]):
                opt1 = self.isPalindrome(s[i+1:j+1])
                opt2 = self.isPalindrome(s[i:j])
                return opt1 or opt2
            i += 1
            j -= 1
        return True