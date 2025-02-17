class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cnt = 0
        g.sort()
        s.sort()

        m,n = 0,0
        while m<len(g) and n<len(s):
            if g[m]<=s[n]:
                cnt +=1
                m +=1
                n +=1
            else:
                n +=1 # Try the next larger cookie
        return cnt