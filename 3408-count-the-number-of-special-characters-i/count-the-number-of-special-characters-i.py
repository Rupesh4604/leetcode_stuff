class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ds = dict()
        chars = list(set(word))
        chars = [ord(char) for char in chars]
        chars.sort()
        left = 0
        right = len(chars)-1
        count = 0
        for i in range(len(chars)-1):
            for j in range(i,len(chars)):
                if chars[j]-chars[i]==32:
                    count+=1
        return count


        

