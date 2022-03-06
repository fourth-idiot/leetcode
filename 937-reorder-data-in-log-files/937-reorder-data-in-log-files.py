class Solution:
    def customComparator(self, log1, log2):
        idx1, log1 = log1
        identifier1, content1 = log1.split(" ", 1)
        idx2, log2 = log2
        identifier2, content2 = log2.split(" ", 1)
        isAlpha1 = "".join(content1.split(" ")).isalpha()
        isAlpha2 = "".join(content2.split(" ")).isalpha()
        if((isAlpha1) and (isAlpha2)):
            if(content1 == content2):
                if(identifier1 < identifier2):
                    return -1
                elif(identifier1 == identifier2):
                    return 0
                else:
                    return 1
            else:
                if(content1 < content2):
                    return -1
                else:
                    return 1
        elif(isAlpha1):
            return -1
        elif(isAlpha2):
            return 1
        else:
            return idx1 - idx2
        
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs = [(i, val) for i, val in enumerate(logs)]
        logs.sort(key=functools.cmp_to_key(self.customComparator))
        logs = [log[1] for log in logs]
        return logs