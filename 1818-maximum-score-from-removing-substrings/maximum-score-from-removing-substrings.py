class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(s, first, second, score):
            stack = []
            temp_score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    temp_score += score
                else:
                    stack.append(char)
            return ''.join(stack), temp_score
        
        if x > y:
            s, score1 = remove_pairs(s, 'a', 'b', x)
            _, score2 = remove_pairs(s, 'b', 'a', y)
        else:
            s, score1 = remove_pairs(s, 'b', 'a', y)
            _, score2 = remove_pairs(s, 'a', 'b', x)
        
        return score1 + score2