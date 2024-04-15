class Solution:
    def maxDepth(self, s: str) -> int:
        maxcount = 0
        count = 0
        for char in s:
            if char=='(':
                count += 1 
            elif char==')':
                if count:
                    count -=1
            if count > maxcount :
                maxcount = count 
        return maxcount 
