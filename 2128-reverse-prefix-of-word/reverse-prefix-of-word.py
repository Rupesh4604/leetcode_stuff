class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx==-1:
            return word
        newstr = "".join(reversed(word[:idx+1]))+word[idx+1:]
        return newstr