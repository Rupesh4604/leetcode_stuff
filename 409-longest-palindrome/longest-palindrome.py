from collections import Counter 
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ds =  Counter(s)
        ans = 0
        for char, counts in ds.items():
            if counts%2==0:
                ans += counts
            else:
                ans += (counts-1)
        # There could be a odd letter in the middle of the palindrome 
        if ans<len(s):
            ans+=1
        return ans