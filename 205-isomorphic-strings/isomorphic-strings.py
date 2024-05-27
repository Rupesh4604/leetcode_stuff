from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        dtwo = {}
        for i in range(len(s)):
            # if the char at position i is not present in the maps add them, if already present then they need to be same as the assigned before. 
            if s[i] not in d1 and t[i] not in dtwo:
                d1[s[i]] = t[i]
                dtwo[t[i]] = s[i]
            elif d1.get(s[i]) != t[i] or dtwo.get(t[i]) != s[i]:
                return False
        return True


