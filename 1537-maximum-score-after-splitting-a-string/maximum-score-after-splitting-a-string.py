class Solution:
    def maxScore(self, s: str) -> int:
        l = len(s)
        max_score = 0
        
        # Initialize counts for first split (first char | rest)
        left_zeros = 1 if s[0] == '0' else 0
        right_ones = s[1:].count('1')
        max_score = left_zeros + right_ones
        
        # Try each split position, except the last character
        # (need to keep right substring non-empty)
        for i in range(1, l-1):
            if s[i] == '0':
                left_zeros += 1  # Add zero to left count
            else:
                right_ones -= 1  # Remove one from right count
            curr_score = left_zeros + right_ones
            max_score = max(max_score, curr_score)
            
        return max_score
