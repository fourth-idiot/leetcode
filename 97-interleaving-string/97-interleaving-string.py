class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def helper(i, j, k):
            # If we reached at the end of s3,
            # then it is possible to interleave s1 and s2 to form s3
            if(k == len(s3)):
                dp[(i, j, k)] = True
                return dp[(i, j, k)]
            # Else if we have reached the end of s2,
            # then we need to compare char from s1 with char from s3
            elif(j == len(s2)):
                if((i + 1, j, k + 1) not in dp):
                    dp[(i + 1, j, k + 1)] = helper(i + 1, j, k + 1)
                return (s1[i] == s3[k]) and dp[(i + 1, j, k + 1)]
            # Else if we have reached the end of s1,
            # then we need to compare char from s2 with char from s3
            elif(i == len(s1)):
                if((i, j + 1, k + 1) not in dp):
                    dp[(i, j + 1, k + 1)] = helper(i, j + 1, k + 1)
                return (s2[j] == s3[k]) and dp[(i, j + 1, k + 1)]
            
            # Take a break, you've reached a milestone :)
            # Now we are sure that none of the strings have reached their ends,
            # so we can compare char from s1 with char from s3, and char from s3 with char from s3
            # If char from s3 do not match with chars from s1 and s3
            if((s1[i] != s3[k]) and (s2[j] != s3[k])):
                dp[(i, j, k)] = False
                return dp[(i, j, k)]
            # Else if char from s3 match with char from s1
            elif(s2[j] != s3[k]):
                if((i + 1, j, k + 1) not in dp):
                    dp[(i + 1, j, k + 1)] = helper(i + 1, j, k + 1)
                return dp[(i + 1, j, k + 1)]
            # Else if char from s3 match with char from s2
            elif(s1[i] != s3[k]):
                if((i, j + 1, k + 1) not in dp):
                    dp[(i, j + 1, k + 1)] = helper(i, j + 1, k + 1)
                return dp[(i, j + 1, k + 1)]
            # Else if char from s3 match with char from s1 and char from s2,
            # the explore both of the options
            else:
                if((i + 1, j, k + 1) not in dp):
                    dp[(i + 1, j, k + 1)] = helper(i + 1, j, k + 1)
                if((i, j + 1, k + 1) not in dp):
                    dp[(i, j + 1, k + 1)] = helper(i, j + 1, k + 1)
                return dp[(i + 1, j, k + 1)] or dp[(i, j + 1, k + 1)]
        
        dp = {}
        if(len(s1) + len(s2) != len(s3)):
            return False
        return helper(0, 0, 0)