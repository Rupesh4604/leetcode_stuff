class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        ans = []
        start = 0
        for i in range(len(s)):
            if s[i]=='(':
                count +=1
            elif s[i]==')':
                count-=1
            if count==0:
                ans.append(s[start+1:i])
                start = i+1
        res = ''.join(ans)
        return res
