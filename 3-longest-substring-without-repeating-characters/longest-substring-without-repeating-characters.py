class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        bag = {}
        start = 0
        stop = 0
        maxlength = 0
        for char in s:
            if char not in bag:
                bag[char] = 1
                stop +=1
                maxlength = max(maxlength,stop-start)
            else:
                while s[start] != char:
                    del bag[s[start]]
                    start += 1
                start += 1
                stop += 1
        return maxlength