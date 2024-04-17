class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        # j = 0
        # start = 0
        # if len(haystack) < len(needle):
        #     return -1
        # for i in range(len(haystack)):
        #     if haystack[i]==needle[0] and j == 0: # start matching 
        #         start = i
        #         j+=1
        #     elif j==len(needle):
        #         return start
        #     elif haystack[i]==needle[j] and j!=0: #matching 
        #         j+=1
        #     elif haystack[i]!=needle[j] and j<len(needle): # not a match 
        #         j = 0
        #         start = 0

        # if j == len(needle):  # Check if needle is found at the end of haystack
        #     return start
        # return -1

        