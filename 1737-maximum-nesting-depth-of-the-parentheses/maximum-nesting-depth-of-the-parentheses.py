class Solution:
    def maxDepth(self, s: str) -> int:
        maxcount = 0
        count = 0
        for char in s:
            if char=='(':
                count += 1 
            maxcount = max(maxcount,count)
            if char==')':
                if count:
                    count -=1
        return maxcount 
