import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = int(math.sqrt(c))
        
        while low <= high:
            current_sum = low**2 + high**2
            if current_sum == c:
                return True
            elif current_sum < c:
                low += 1
            else:
                high -= 1
        
        return False