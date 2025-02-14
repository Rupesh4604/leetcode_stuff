class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        t1 = t2 = -1
        count = 0

        for i in range(n):
            if s1[i]!=s2[i]:
                count +=1
                if t1!=-1:
                    t2=i
                else:
                    t1 = i
        
        if count>2:
            return False
        
        if s1[t1]==s2[t2] and s1[t2]==s2[t1]: # works for both count=0 and count=2 
            return True
        ## count=2 but different chars
        return False


