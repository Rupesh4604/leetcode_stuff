class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        low = 0
        high = len(tokens)-1 
        max_score = 0
        if tokens == []:
            return 0
        if power < tokens[low]:
            return 0
        while low <= high :
            if power >= tokens[low]:
                power -= tokens[low]
                score += 1
                max_score = max(max_score,score)
                low +=1
            elif score>0 :
                power += tokens[high]
                score -= 1
                high -=1
            else:
                break
        return max_score

            

            
              