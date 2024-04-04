class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        arr = s.split()
        length = len(arr[-1])
        return length