from collections import Counter  
class Solution:
    def minimumPushes(self, word: str) -> int:
        # Initialize frequency array for 26 letters
        freq = [0] * 26

        # Calculate frequency of each character in the word
        for c in word:
            freq[ord(c) - ord('a')] += 1

        # Sort frequencies in descending order
        freq.sort(reverse=True)

        # Calculate minimum pushes
        sz = 0
        push = 1
        ans = 0
        while sz < 26 and freq[sz] != 0:
            if sz >= 8 and sz % 8 == 0:
                push += 1
            ans += freq[sz] * push
            sz += 1

        return ans