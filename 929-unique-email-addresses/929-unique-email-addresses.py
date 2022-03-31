class Solution:
    def preprocess(self, s):
        isDomain = False
        isSkip = False
        modifiedS = []
        for c in s:
            if(c == "@"):
                isSkip = False
                isDomain = True
            if((isSkip) or
               ((c == ".") and (not isDomain))):
                continue
            elif(c == "+"):
                isSkip = True
                continue
            modifiedS.append(c)
        return "".join(modifiedS)
    
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            uniqueEmails.add(self.preprocess(email))
        return len(uniqueEmails)